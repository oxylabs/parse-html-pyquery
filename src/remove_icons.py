from pyquery import PyQuery as pq

doc = pq(url="https://books.toscrape.com")
for icon in doc("i"):
   icon.remove()