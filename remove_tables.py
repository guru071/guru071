import re

with open("README.md", "r") as f:
    c = f.read()

# I will just remove the specific table tags.
c = re.sub(r'<table.*?>', '<div align="center">', c)
c = c.replace('</table>', '</div>')
c = re.sub(r'<td.*?>', '', c)
c = c.replace('</td>', '')
c = re.sub(r'<tr.*?>', '', c)
c = c.replace('</tr>', '')

# Clean up empty lines
c = re.sub(r'\n\s*\n', '\n\n', c)

with open("README.md", "w") as f:
    f.write(c)
