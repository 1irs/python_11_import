from urllib.parse import urlparse
from urllib.parse import quote, unquote



url = 'https://docs.python.org/3/library/urllib.parse.html?login=vladimir&session_id=123#tag1'

print(urlparse(url))

original = 'Vladimir Obrizan?-+'

print(quote(original))

source = 'https://serverName/deepLinkAction.do?userName=peter%40nable%2Ecom&password=Hello%25There&method=defaultDashboard'

print(source)
print(unquote(source))
