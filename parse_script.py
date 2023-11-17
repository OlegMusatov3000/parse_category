import requests
import csv

from constants import (
    MAIN_URL, HEADERS, COOKIES_FOR_MOSCOW, PARAMS, CATEGORY_EXAMPLE,
    WRONG_CATEGORY, COOKIES_FOR_SAINT_PETERSBURG
)
from utils import (
    get_last_page, get_all_products_in_cur_page, get_all_attribute_for_item
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

        last_page = get_last_page(start_response)
        if last_page == WRONG_CATEGORY:
            print(WRONG_CATEGORY)
            return WRONG_CATEGORY

        for page in range(1, int(last_page) + 1):

            url = f'{category_url}&page={page}'
            if url != start_url:
                response = requests.get(
                    f'{category_url}&page={page}', headers=HEADERS,
                    cookies=COOKIES_FOR_SAINT_PETERSBURG, params=PARAMS
                )
            else:
                response = start_response

            products = get_all_products_in_cur_page(response.text)

            for item in products:
                (
                    id, product_name, product_link,
                    product_price, discount_price, brand_name
                ) = get_all_attribute_for_item(item)

                all_products.append(
                    [
                        id, product_name, product_link,
                        product_price, discount_price, brand_name
                    ]
                )

    return all_products


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'id товара', 'наименование', 'ссылка на товар',
            'регулярная цена', 'промо цена', 'бренд'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for values in data:
            writer.writerow({
                'id товара': values[0],
                'наименование': values[1],
                'ссылка на товар': values[2],
                'регулярная цена': values[3],
                'промо цена': values[4],
                'бренд': values[5]
            })


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
