from urllib.request import urlopen

try:
    html = urlopen("http://www.aiub.ed")
    print(html.read().decode('utf-8'))
# print(html.read())

## 100 chars with UTF decode
# print(html.read(100).decode('utf-8'))
except:
    print("SOmething wrong")
