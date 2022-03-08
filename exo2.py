import re

with open("exo2/exo2.txt") as f:
    content = f.read()
    
tab = re.findall(r".*\n", content)
print(tab)
