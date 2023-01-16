from pyquery import PyQuery as pq

doc = pq(url="https://books.toscrape.com")
for link in doc("h3>a"):
   print(link.text, link.attrib["href"])