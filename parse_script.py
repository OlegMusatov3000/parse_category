import requests
from bs4 import BeautifulSoup as bt
import csv

from constants import (
    MAIN_URL, HEADERS, COOKIES_FOR_MOSCOW, PARAMS, CATEGORY_EXAMPLE,
    WRONG_CATEGORY, COOKIES_FOR_SAINT_PETERSBURG
)


def parse_metro_category(category_url):
    start_url = f'{category_url}&page=1'
    all_products = []
    print(f'Начинаю парсить товары с ресурса:\n{start_url}')
    for cookies_for_city in [COOKIES_FOR_MOSCOW, COOKIES_FOR_SAINT_PETERSBURG]:
        if cookies_for_city == COOKIES_FOR_MOSCOW:
            print('начинаю парсить товары из города Москва')
        else:
            print('начинаю парсить товары из города Санкт-Петербург')
        start_response = requests.get(
            start_url, headers=HEADERS,
            cookies=cookies_for_city, params=PARAMS
        )

        soup = bt(start_response.text, 'lxml')
        list_items = soup.find_all('li', {'data-v-2505d9ee': True})
        try:
            last_pages = list_items[-2].get_text(strip=True)
        except IndexError:
            print(WRONG_CATEGORY)
            return WRONG_CATEGORY

        for page in range(1, int(last_pages) + 1):
            print(page)
            url = f'{category_url}&page={page}'
            if url != start_url:
                response = requests.get(
                    f'{category_url}&page={page}', headers=HEADERS,
                    cookies=COOKIES_FOR_SAINT_PETERSBURG, params=PARAMS
                )
            else:
                response = start_response

            soup = bt(response.text, 'lxml')
            products = soup.find_all(class_=('catalog-2-level-product-card product-card subcategory-or-type__products-item with-rating with-prices-drop has-online-range-prices', 'catalog-2-level-product-card product-card subcategory-or-type__products-item with-rating with-prices-drop', 'catalog-2-level-product-card product-card subcategory-or-type__products-item with-rating has-cashback with-prices-drop has-online-range-prices'))
            print(len(products))
            for place, item in enumerate(products):
                print(place + 1)
                link_element = item.find('a', class_='product-card-photo__link')
                product_link = link_element.get('href')[1:]

                is_promotion = item.find('span', class_='product-price nowrap product-unit-prices__actual style--catalog-2-level-product-card-major-actual color--red')

                rubles = item.find('span', class_='product-price__sum-rubles').get_text(strip=True)
                penny = item.find('span', class_='product-price__sum-penny')
                if penny:
                    penny = penny.get_text(strip=True)
                    product_price = f'{rubles}{penny}'
                    # print(penny)
                else:
                    product_price = rubles

                if is_promotion:
                    discount_price = product_price
                    product_price = item.find('div', class_='product-unit-prices__old-wrapper')
                    if product_price:
                        old_price_in_rubles = product_price.find('span', class_='product-price__sum-rubles')
                        old_price_in_penny = product_price.find('span', class_='product-price__sum-penny')
                        if old_price_in_rubles and old_price_in_penny:
                            old_price_in_rubles = old_price_in_rubles.get_text(strip=True)
                            old_price_in_penny = old_price_in_penny.get_text(strip=True)
                            product_price = f'{old_price_in_rubles}{old_price_in_penny}'
                        elif old_price_in_rubles:
                            product_price = old_price_in_rubles.get_text(strip=True)
                        else:
                            product_price = old_price_in_rubles
                else:
                    discount_price = None
                print(f'обычная цена: {product_price}')
                print(f'цена по скидке: {discount_price}')

                response = requests.get(
                    f'{MAIN_URL}{product_link}', headers=HEADERS,
                    cookies=COOKIES_FOR_MOSCOW, params=PARAMS
                )
                soup = bt(response.text, 'lxml')

                id_element = soup.find('p', class_='product-page-content__article')
                id = id_element.get_text(strip=True).split(' ')[-1]

                name_element = soup.find('meta', {'itemprop': 'name'})
                product_name = name_element.get('content')

                brand_element = soup.find('a', class_=('product-attributes__list-item-link reset-link active-blue-text'))
                brand_name = brand_element.get_text(strip=True)

                all_products.append(
                    [id, product_name, product_link, product_price, discount_price, brand_name]
                )

    len(all_products)
    return all_products


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id товара', 'наименование', 'ссылка на товар', 'регулярная цена', 'промо цена', 'бренд']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for values in data:
            writer.writerow({'id товара': values[0], 'наименование': values[1], 'ссылка на товар': values[2], 'регулярная цена': values[3], 'промо цена': values[4], 'бренд': values[5]})


if __name__ == "__main__":
    category = input('''Введите правильное имя категории для парсера пример:\n
category/molochnye-prodkuty-syry-i-yayca/syry/plavlenye \n
Вы можете скопировать его из адресной строки на странице со списками
товаров, можете нажать 1 и будет применена категория из примера:
''')
    if category == '1':
        category = CATEGORY_EXAMPLE
    category_url = f"{MAIN_URL}{category}?from=under_search"
    products = parse_metro_category(category_url)

    if products is not WRONG_CATEGORY and len(products) > 100:
        print("Более 100 товаров в категории. Сохранение данных.")
        save_to_csv(products, 'metro_products.csv')
    else:
        print("Сохранение отменено.")
