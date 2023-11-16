import requests
from bs4 import BeautifulSoup as bt
import csv

from constants import MAIN_URL, HEADERS, COOKIES, PARAMS


def parse_auchan_category(category_url):

    last_pages = 24
    all_products = []
    for page in range(6, last_pages + 1):
        print(page)
        response = requests.get(f'{category_url}&page={page}', headers=HEADERS, cookies=COOKIES, params=PARAMS)
        soup = bt(response.text, 'lxml')
        products = soup.find_all(class_=('catalog-2-level-product-card product-card subcategory-or-type__products-item with-rating with-prices-drop has-online-range-prices', 'catalog-2-level-product-card product-card subcategory-or-type__products-item with-rating with-prices-drop', 'catalog-2-level-product-card product-card subcategory-or-type__products-item with-rating has-cashback with-prices-drop has-online-range-prices'))
        for item in products:
            link_element = item.find('a', class_='product-card-photo__link')
            product_link = link_element.get('href')[1:]
            print(f'{MAIN_URL}{product_link[1:]}')

            price_span = soup.find('span', class_='product-price__sum-rubles')
            price = price_span.get_text(strip=True).replace(' ', '')
            print(price)
            # product_id = item.get('data-sku')
            # print(product_id)
            response = requests.get(f'{MAIN_URL}{product_link}', headers=HEADERS, cookies=COOKIES, params=PARAMS)
            soup = bt(response.text, 'lxml')
            # short_info = soup.find_all(class_='product-attributes__list style--product-page-short-list')
            # print
            id_element = soup.find('p', class_='product-page-content__article')
            id = id_element.get_text(strip=True).split(' ')[-1]

            name_element = soup.find('meta', {'itemprop': 'name'})
            product_name = name_element.get('content')

            brand_element = soup.find('a', class_='product-attributes__list-item-link reset-link active-blue-text')
            brand_name = brand_element.get_text(strip=True)


            # brand = short_info.find('a', class_='product-attributes__list-item-link reset-link active-blue-text')
            print(id)
            print(product_name)
            print(brand_name)
            
            break
        break
        print(len(all_products))
    print(len(all_products))
    # for item in all_products:
    #     item_id = item['data-offer-id']
    
    #     # Получаем текст внутри тега 'p'
    #     title = item.find('p').text.strip()
        
    #     # Получаем атрибут href из тега 'a'
    #     link = item.find('a')['href']
        
    #     # Ищем цену и валюту внутри тега 'div' с классом 'css-xtv3eo'
    #     price_element = item.find('div', class_='css-xtv3eo')
    #     price = price_element.text.strip()

        
    #     # Получаем атрибут brand из скрипта с типом "application/ld+json"
    #     script_data = item.find('script', type='application/ld+json').text
    #     brand_start = script_data.find('"brand"') + 8
    #     brand_end = script_data.find('"', brand_start)
    #     brand = script_data[brand_start:brand_end]
        
    #     # Выводим полученные данные
    #     print(f"Item ID: {item_id}")
    #     print(f"Title: {title}")
    #     print(f"Link: {MAIN_URL}{link}")
    #     print(f"Price: {price}")
    #     print(f"Brand: {brand}")
    #     print("\n")
    #     break

    products = []
    return products


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'name', 'link', 'regular_price', 'promo_price', 'brand']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    category_url = f"{MAIN_URL}category/molochnye-prodkuty-syry-i-yayca/syry?from=under_search"  # Замените на фактический URL категории товаров
    products = parse_auchan_category(category_url)

    if len(products) > 100:
        print("Более 100 товаров в категории. Сохранение данных.")
        save_to_csv(products, 'metro_products.csv')
    else:
        print("Менее 100 товаров в категории.")


# import requests
# from bs4 import BeautifulSoup
# import csv
# import json

# def parse_auchan_cheeses(category_url, headers, cookies):
#     response = requests.get(category_url, headers=headers, cookies=cookies)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     cheeses = []

#     for cheese_card in soup.find_all('div', class_='cheese-card'):
#         # Извлекаем необходимые данные
#         cheese_id = cheese_card.find('script', type='application/ld+json').text.strip()
#         cheese_id = json.loads(cheese_id).get('offers', {}).get('sku')
        
#         name = cheese_card.find('p', class_='css-1bdovxp').text.strip()
#         link = cheese_card.find('a', class_='linkToPDP').get('href')
#         regular_price = cheese_card.find('div', class_='css-xtv3eo').text.strip()
#         promo_price = cheese_card.find('div', class_='css-1hxq85i').text.strip() if cheese_card.find('div', class_='css-1hxq85i') else None
#         brand = json.loads(cheese_card.find('script', type='application/ld+json').text.strip()).get('brand')

#         # Проверяем наличие сыра
#         availability = cheese_card.find('span', class_='cheese-card__availability').text.strip()
#         if availability.lower() == 'в наличии':
#             cheeses.append({
#                 'id': cheese_id,
#                 'name': name,
#                 'link': link,
#                 'regular_price': regular_price,
#                 'promo_price': promo_price,
#                 'brand': brand
#             })

#     return cheeses

# def save_to_csv(data, filename):
#     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['id', 'name', 'link', 'regular_price', 'promo_price', 'brand']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()
#         for row in data:
#             writer.writerow(row)

# if __name__ == "__main__":
#     category_url = "https://www.auchan.ru/catalog/syry/tverdye-i-polutverdye/"  # Замените на фактический URL категории с сырами
#     cheeses = parse_auchan_cheeses(category_url, headers, cookies)

#     if len(cheeses) > 0:
#         print("Сохранение данных о сырах.")
#         save_to_csv(cheeses, 'auchan_cheeses.csv')
#     else:
#         print("Нет данных о сырах.")
