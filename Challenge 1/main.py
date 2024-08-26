content = []
text = input()
z = []
#print(content)

while text != "..":
    content.append(text)
    text = input()

length = len(content)
x = ""
p = 0

print("""<html>
<head>
<body>""")

for n in content:
    y = x
    y += "<p>" + str(n) + "</p>"
    print(y)

print("""</body>
</html>""")

