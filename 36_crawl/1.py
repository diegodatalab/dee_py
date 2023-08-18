from urllib.request import urlopen

x = urlopen("http://www.wikipedia.org")

print(x.read())
