MAIN_URL = 'https://online.metro-cc.ru/'
CATEGORY_EXAMPLE = 'category/molochnye-prodkuty-syry-i-yayca/syry/plavlenye'

HEADERS = {
    'authority': 'online.metro-cc.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_slid_server=6555c114515748bbf2024e28; exp_auth=3Rd5fv0vTUylyTasdzAcqA.1; is18Confirmed=false; _slfs=1700118804136; _slid=6555c114515748bbf2024e28; _slsession=A5F93936-5B5B-4A6B-B1B2-C79D807740C3; _slfreq=633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1700126005%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1700126005%3B6490039afadf0f1d430966df%3A64e35a6b6c71a1d5090937fb%3A1700126005; metro_user_id=3d4e4f37f16802a8a1794cce5d9a72ee; _ga=GA1.1.1202858113.1700118805; uxs_uid=a25730d0-844f-11ee-a782-8fe7d6f321e9; _ym_uid=1700118806886464201; _ym_d=1700118806; _ym_isad=2; _ym_visorc=w; _gcl_au=1.1.1248662484.1700118806; tmr_lvid=ea0b1709a077d32f473173fe5e4a8e1a; tmr_lvidTS=1700118806631; flocktory-uuid=f8bc22ed-37a7-43e9-9684-8fb4ba9f2848-8; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; metroStoreId=10; sl_anh=1; mp_6d4d5c2aa2170f906c84f873ab89181b_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18bd6fa3c652dab-0df411911412bb-16525634-13c680-18bd6fa3c652dab%22%2C%22%24device_id%22%3A%20%2218bd6fa3c652dab-0df411911412bb-16525634-13c680-18bd6fa3c652dab%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; _ga_VHKD93V3FV=GS1.1.1700118805.1.1.1700119141.0.0.0; mindboxDeviceUUID=cde0e97a-3cf7-436a-a284-ba1a08d0918a; directCrm-session=%7B%22deviceGuid%22%3A%22cde0e97a-3cf7-436a-a284-ba1a08d0918a%22%7D; tmr_detect=0%7C1700119143203',
    'if-none-match': '"1efbb8-IL3TX+a3ZjH19RawWfOwzKZDUEU"',
    'referer': 'https://online.metro-cc.ru/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

COOKIES_FOR_MOSCOW = {
    '_slid_server': '6555c114515748bbf2024e28',
    'exp_auth': '3Rd5fv0vTUylyTasdzAcqA.1',
    'is18Confirmed': 'false',
    '_slfs': '1700118804136',
    '_slid': '6555c114515748bbf2024e28',
    '_slsession': 'A5F93936-5B5B-4A6B-B1B2-C79D807740C3',
    '_slfreq': '633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1700126005%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1700126005%3B6490039afadf0f1d430966df%3A64e35a6b6c71a1d5090937fb%3A1700126005',
    'metro_user_id': '3d4e4f37f16802a8a1794cce5d9a72ee',
    '_ga': 'GA1.1.1202858113.1700118805',
    'uxs_uid': 'a25730d0-844f-11ee-a782-8fe7d6f321e9',
    '_ym_uid': '1700118806886464201',
    '_ym_d': '1700118806',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    '_gcl_au': '1.1.1248662484.1700118806',
    'tmr_lvid': 'ea0b1709a077d32f473173fe5e4a8e1a',
    'tmr_lvidTS': '1700118806631',
    'flocktory-uuid': 'f8bc22ed-37a7-43e9-9684-8fb4ba9f2848-8',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'metroStoreId': '10',
    'sl_anh': '1',
    'mp_6d4d5c2aa2170f906c84f873ab89181b_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18bd6fa3c652dab-0df411911412bb-16525634-13c680-18bd6fa3c652dab%22%2C%22%24device_id%22%3A%20%2218bd6fa3c652dab-0df411911412bb-16525634-13c680-18bd6fa3c652dab%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D',
    '_ga_VHKD93V3FV': 'GS1.1.1700118805.1.1.1700119141.0.0.0',
    'mindboxDeviceUUID': 'cde0e97a-3cf7-436a-a284-ba1a08d0918a',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22cde0e97a-3cf7-436a-a284-ba1a08d0918a%22%7D',
    'tmr_detect': '0%7C1700119143203',
}

COOKIES_FOR_SAINT_PETERSBURG = {
    '_slid_server': '6555c114515748bbf2024e28',
    '_slid_server': '6555c114515748bbf2024e28',
    'exp_auth': '3Rd5fv0vTUylyTasdzAcqA.1',
    'is18Confirmed': 'false',
    '_slid': '6555c114515748bbf2024e28',
    'metro_user_id': '3d4e4f37f16802a8a1794cce5d9a72ee',
    '_ga': 'GA1.1.1202858113.1700118805',
    'uxs_uid': 'a25730d0-844f-11ee-a782-8fe7d6f321e9',
    '_ym_uid': '1700118806886464201',
    '_ym_d': '1700118806',
    '_ym_isad': '2',
    '_gcl_au': '1.1.1248662484.1700118806',
    'tmr_lvid': 'ea0b1709a077d32f473173fe5e4a8e1a',
    'tmr_lvidTS': '1700118806631',
    'flocktory-uuid': 'f8bc22ed-37a7-43e9-9684-8fb4ba9f2848-8',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'sl_anh': '1',
    '_slfreq': '633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1700157762%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1700157762%3B6490039afadf0f1d430966df%3A64e35a6b6c71a1d5090937fb%3A1700126005',
    'mp_6d4d5c2aa2170f906c84f873ab89181b_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18bd6fa3c652dab-0df411911412bb-16525634-13c680-18bd6fa3c652dab%22%2C%22%24device_id%22%3A%20%2218bd6fa3c652dab-0df411911412bb-16525634-13c680-18bd6fa3c652dab%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D',
    'tmr_detect': '0%7C1700150728083',
    'mindboxDeviceUUID': 'cde0e97a-3cf7-436a-a284-ba1a08d0918a',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22cde0e97a-3cf7-436a-a284-ba1a08d0918a%22%7D',
    'pickupStore': '15',
    'metroStoreId': '15',
    '_ga_VHKD93V3FV': 'GS1.1.1700182195.5.1.1700182224.0.0.0',
}


PARAMS = {
    'from': 'under_search',
}
CLASSES_FOR_FIDE = (
        'catalog-2-level-product-card product-card subcategory-or-type__products-item with-rating with-prices-drop has-online-range-prices',
        'catalog-2-level-product-card product-card subcategory-or-type__products-item with-rating with-prices-drop',
        'catalog-2-level-product-card product-card subcategory-or-type__products-item with-rating has-cashback with-prices-drop has-online-range-prices'
    )
CLASS_FOR_GET_PRICES = 'product-price nowrap product-unit-prices__actual style--catalog-2-level-product-card-major-actual color--red'

WRONG_CATEGORY = (
    'Кажется, вы указали неправильную категорию. Пожалуйста,'
    ' запустите скрипт снова и введите корректное название категории.'
)
