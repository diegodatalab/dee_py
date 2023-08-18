from urllib.request import urlopen
from bs4 import BeautifulSoup

x = urlopen("http://www.wikipedia.org")

bs_object = BeautifulSoup(x.read(), "html.parser")

print(bs_object.h1)
print()
print(bs_object.title)

