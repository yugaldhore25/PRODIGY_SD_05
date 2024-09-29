import requests
from bs4 import BeautifulSoup
import pandas as pd

print('\n'"TASK:-5")
print('\n'"This code is represented by Yugal Dhore.")
print('\n'"------WEB SCRAPING------")

# URL and the page range
url = "https://www.flipkart.com/search?q=shoes+for+men&sid=osp%2Ccil&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=shoes+for+men%7CMen%27s+Footwear&requestId=dc140038-1499-4d51-bee9-3ab1e8d82172&as-searchtext=shoes+for+men&page=2"
startPage = 1
endPage = 20
data = []

for page in range(startPage, endPage + 1):
    print(f"Scraping page {page}...")
    req_response = requests.get(url.format(page))
    soup = BeautifulSoup(req_response.text, 'html.parser')

# Data extraction from each shoes
    shoes1 = soup.find_all('article', class_='product_pod')
    for shoes in shoes1:
        shoesTitle = shoes.find("h3").text.strip()
        shoesPrice = shoes.find("p", class_='price_color').text.strip()
        shoesRating = shoes.find("p", class_='star-rating').get('class')[1]
        shoesAvailability = shoes.find("p", class_='availability').text.strip()
# Adding the extracted data to the list
        data.append({
            "shoes Title": shoesTitle,
            "Price": shoesPrice,
            "Rating": shoesRating,
            "Availability": shoesAvailability
        })

    print(f"Page {page} scraped successfully!")
df = pd.DataFrame(data)
df.to_csv('shoes_data.csv', index=False, encoding='utf-8')
print("Data extraction complete!")
print("CSV file saved to shoes_data.csv")
