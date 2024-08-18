import markdown

# Read the markdown file
with open("main.md", 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(md_content)

# HTML structure
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="VF2UhQRwBF9gSN1h_VSAFunEopndMFD076grR5ofVkk" />
    <meta name="description" content="Alek Westover's personal website">
    <meta name="author" content="Alek Westover">
    <meta name="robots" content="index,follow">
    <title>Alek Westover</title>
    <link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
<main>
    {html_content}
</main>
</body>
</html>
"""

# Write the HTML output to a file
with open("index.html", 'w', encoding='utf-8') as f:
    f.write(html_template)


