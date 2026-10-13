"""Refresh the LessWrong post list in README.md from the LessWrong API.

Posts with >= KARMA_THRESHOLD karma come first, then the rest; each group is newest first.
Run `python3 compile.py` afterwards to regenerate index.html.
"""
import html
import json
import re
import urllib.request

USER_SLUG = "alek-westover"
KARMA_THRESHOLD = 40
GRAPHQL_URL = "https://www.lesswrong.com/graphql"


def graphql(query):
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=json.dumps({"query": query}).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)["data"]


user_id = graphql(
    f'{{ user(input:{{selector:{{slug:"{USER_SLUG}"}}}}){{ result {{ _id }} }} }}'
)["user"]["result"]["_id"]

posts = graphql(
    f'{{ posts(input:{{terms:{{view:"userPosts", userId:"{user_id}", limit:1000}}}})'
    "{ results { title baseScore postedAt pageUrl shortform } } }"
)["posts"]["results"]
posts = [p for p in posts if not p["shortform"]]
posts.sort(key=lambda p: p["postedAt"], reverse=True)
posts.sort(key=lambda p: p["baseScore"] < KARMA_THRESHOLD)  # stable: keeps date order within groups

items = "\n".join(
    f'<li><a href="{html.escape(p["pageUrl"])}">{html.escape(" ".join(p["title"].split()))}</a></li>'
    for p in posts
)

with open("README.md", encoding="utf-8") as f:
    readme = f.read()
new_readme, n = re.subn(
    r'(<ul id="lw-posts">\n).*?(\n</ul>)', lambda m: m[1] + items + m[2], readme, flags=re.DOTALL
)
assert n == 1, f'expected exactly one <ul id="lw-posts"> block in README.md, found {n}'
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

n_high = sum(p["baseScore"] >= KARMA_THRESHOLD for p in posts)
print(f"Wrote {len(posts)} posts ({n_high} with >= {KARMA_THRESHOLD} karma) to README.md")
