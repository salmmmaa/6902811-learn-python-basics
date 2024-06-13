# Write your code here!
from bs4 import BeautifulSoup

with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

title = soup.title.string

h1_text = soup.h1.string

products = soup.find_all('li')
products_list = []
for product in products:
    name = product.h2.string
    price = product.find('p', string=lambda s: 'Price' in s).string
    products_list.append((name, price))

descriptions_list = []
for product in products:
    description = product.find('p', string=lambda s: 'Description' in s).string
    descriptions_list.append(description)

print("Title of the page :", title)
print("Text of the h1 tag :", h1_text)
print("Product list :", products_list)
print("List of product descriptions :", descriptions_list)

for i, (name, price) in enumerate(products_list):
    euro_price = int(price.split()[2].replace("€",""))
    dollar_price = euro_price * 1.2
    products_list[i] = (name, f"{dollar_price}$")

print("List of products :", products_list)
