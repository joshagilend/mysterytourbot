Index = open("index.html", "w")

html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <title>mysterytourbot</title>
  </head>
  <body>
    <h1>Hello world</h1>
  </body>
</html>"""

Index.write(html)
Index.close