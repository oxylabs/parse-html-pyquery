import requests
from pyquery import PyQuery as pq
 
r = requests.get("https://example.com")
doc = pq(r.content)
print(doc("title").text())