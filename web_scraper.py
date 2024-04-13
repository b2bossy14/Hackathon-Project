from bs4 import BeautifulSoup
import requests

website = 'https://www.yelp.com/biz/five-guys-lawrence?hrid=r59LI61UjUfSvy7FARONKw'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
review_boxes = soup.find_all('p', class_='comment__09f24__D0cxf css-qgunke')

if review_boxes:
    for review_box in review_boxes:
        review_text = review_box.get_text(strip=True)
        print('\n Review:', review_text)
else:
    print("Not found")

# box = soup.find('article', class_='main-article')

# title = box.find('h1').get_text()

# transcript = box.find('div', class_= 'full-script').get_text(strip=True, separator=' ')
# print(title)
# print(transcript)

