import requests
from bs4 import BeautifulSoup as bt

from constants import (
    MAIN_URL, HEADERS, COOKIES_FOR_MOSCOW, PARAMS,
    WRONG_CATEGORY, CLASSES_FOR_FIDE, CLASS_FOR_GET_PRICES
)


def get_last_page(url):
    soup = bt(url.text, 'lxml')
    list_items = soup.find_all('li', {'data-v-2505d9ee': True})
    try:
        return list_items[-2].get_text(strip=True)
    except IndexError:
        print(WRONG_CATEGORY)
        return WRONG_CATEGORY


def get_all_products_in_cur_page(response_text):
    soup = bt(response_text, 'lxml')
    return soup.find_all(class_=(CLASSES_FOR_FIDE))


def get_link(item):
    link_element = item.find('a', class_='product-card-photo__link')
    return link_element.get('href')[1:]


def get_prices(item):
    is_promotion = item.find('span', class_=CLASS_FOR_GET_PRICES)

    rubles = item.find(
        'span', class_='product-price__sum-rubles'
    ).get_text(strip=True)
    penny = item.find('span', class_='product-price__sum-penny')
    if penny:
        penny = penny.get_text(strip=True)
        product_price = f'{rubles}{penny}'

    else:
        product_price = rubles

    if is_promotion:
        discount_price = product_price
        product_price = item.find(
            'div', class_='product-unit-prices__old-wrapper'
        )
        if product_price:
            old_price_in_rubles = product_price.find(
                'span', class_='product-price__sum-rubles'
            )
            old_price_in_penny = product_price.find(
                'span', class_='product-price__sum-penny'
            )
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

    return product_price, discount_price


def get_detailed_description(product_link):
    response = requests.get(
        f'{MAIN_URL}{product_link}', headers=HEADERS,
        cookies=COOKIES_FOR_MOSCOW, params=PARAMS
    )

    return bt(response.text, 'lxml')


def get_id_item(soup):
    id_element = soup.find('p', class_='product-page-content__article')

    return id_element.get_text(strip=True).split(' ')[-1]


def get_product_name(soup):
    name_element = soup.find('meta', {'itemprop': 'name'})
    return name_element.get('content')


def get_brand_name(soup):
    brand_element = soup.find('a', class_=(
        'product-attributes__list-item-link reset-link active-blue-text'
    ))
    return brand_element.get_text(strip=True)


def get_all_attribute_for_item(item):
    product_link = get_link(item)
    product_price, discount_price = get_prices(item)
    soup = get_detailed_description(product_link)
    id = get_id_item(soup)
    product_name = get_product_name(soup)
    brand_name = get_brand_name(soup)
    return (
        id, product_name, product_link,
        product_price, discount_price, brand_name
    )
