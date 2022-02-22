import html

original = '<html><body><h1>Hello world</h1></body></html>'

# отправить на сайт через комментарии

# прочитать комментарий опубликованый

escaped = html.escape(original)

result = html.unescape(escaped)

print(result)
