from pyquery import PyQuery as pq

doc = pq(url="https://books.toscrape.com")
doc("i").remove()
print(doc)

