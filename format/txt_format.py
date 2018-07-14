
import sys

if len(sys.argv) != 2:
  print("len(sys.argv) != 2")
  sys.exit()

fil = sys.argv[1]
rs = []
with open(fil, "r") as f:
  for r in f:
    rs.append(r)

rgs = []
rgsmd = []
for rr in rs:
  r = rr.strip()
  if len(r) > 0:
    if r[0] == "#":
      x = r.count("#")
      rgs.append("\n<h{}>{}</h{}>".format(x,r[x+1:],x))
      rgsmd.append("\n"+r)
    else:
      rgs.append("  <li>{}</li>".format(r))
      rgsmd.append("  * {}".format(r))

with open(fil.replace(".txt", ".md"), "w") as f:
  f.write("\n".join(rgsmd))

with open(fil.replace(".txt", ".html"), "w") as f:
  f.write("\n".join(rgs))


