# imports
import requests
import pandas as pd

# data that we want to scrape: item name/title, brand, price
# declare arrays for each of these data fields
item_title = []
item_brand = []
item_price = []

# loop through the 4 pages for ground beef search results
# Get page requests using cURL -- each page's cURL offset param increments by 24
# loop increments by 24 -- limit is 72 bc there are only 4 pages (4x24)
for i in range(0, 72, 24):
    cookies = {
        'TealeafAkaSid': 'waL3jgAdhN0XiguU9qg6d0fJcjwDtucM',
        'visitorId': '0180A2D58E740201B23993625ACB1488',
        'sapphire': '1',
        'UserLocation': '91803|34.070|-118.140|CA|US',
        'egsSessionId': '202a9a4a-5cc5-4946-8e08-b5389bc61d05',
        'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI0YWEwZTgwNC0yZGY3LTQyZmQtODUyMy1lOTdjZjZjOTMwOTUiLCJpc3MiOiJNSTYiLCJleHAiOjE2NTIwODU3NDksImlhdCI6MTY1MTk5OTM0OSwianRpIjoiVEdULjNjYzhhYmJjYjg5MDQ2ZDE5ZTg3ZDAwODRjNzc5NWY3LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6Ijc4ZTEzNTdiNjZmZDNmNTllNWM4NWYzOTg4ZjQzNzk5MmMwZmJlYzIxYmFmMDdmMzYyZGI5NTMwNTcxNTRhYmQiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.OlWNDvmAYEm3Wx8fErfOCuxzKmF2Cv-f3LBVrIcgbAVlteuqm6GkbuqEJv49b6j2o8JQoSguPPKV3mErigSVhPBsThZEvLDkxceOaQfBBgPHbn8IP-YxWaXb7zAFiIg9q0FXfqpSjesFNF7eOy7khRiPnFB8Aa0Fmc60mskfEMNwM8I7pUzre1Z_lF5UVB4BeVDWUF2TpMByTHXKmXoLHWzTB410CGEd-hZVkj56c7elVNh7IYyN_H6cWfVyaZje7tQddilZgHbxYfI7dNNPdslr4T-OmWuLRE-XJncyEvOnqtlPjUCXAuURZVMbKgLqoCVSaerc5FkXPiiXP3UaDA',
        'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiI0YWEwZTgwNC0yZGY3LTQyZmQtODUyMy1lOTdjZjZjOTMwOTUiLCJpc3MiOiJNSTYiLCJleHAiOjE2NTIwODU3NDksImlhdCI6MTY1MTk5OTM0OSwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.',
        'refreshToken': 'uGypaLhlWlWT1bIOtIlfu9GTFXnyyDnT27v8WrGIdmGblmME8mcdCJ615GpjdPjDQVrAdnc_RsTfVXqPcK2C1w',
        '__gpi': 'UID=000005603bb0d81d:T=1651999349:RT=1651999349:S=ALNI_MZYAjjnoTaXZKNHWTX3uHodjqlSTg',
        'fiatsCookie': 'DSI_184|DSN_Alhambra|DSZ_91801',
        '_mitata': 'OWVhZmE2YmY4OGMxMDdhYTI2OTUxM2U1Zjc0MjQxNTAwNTQwMmFjZWQzYjZkZWMyYzA5ODg0NjkxMWViNzJhYQ==_/@#/1651999410_/@#/cCVzrt4ugLvrbBGW_/@#/ZjIxYTkwYzAwY2RlYTNiMGEwYmIwZTM4N2JhNDg3MTJjZWVmNTg2ZGM2YTgwN2JhNjMzYmYzOTc5M2QyM2JmYQ==_/@#/000',
        'ci_pixmgr': 'other',
        '_gcl_au': '1.1.1744745437.1651999352',
        '__gads': 'ID=279fd1e6d1b46bbc:T=1651999349:S=ALNI_MZl-WphOYuq372ZYWKy5KuSH0_6xw',
        'ffsession': '{%22sessionHash%22:%221552af6b77b7641651999347791%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=ground+beef&category=0|All|matchallpartial|all%2520categories&tref=typeahead%257Cterm%257Cundefined%257Cground%2520beef%257C%257C%257C%257Cservice%257C%257C%257C%257C&searchTermRaw=groun%22%2C%22sessionHit%22:3%2C%22prevSearchTerm%22:%22ground%20beef%22}',
        '_uetsid': 'ccac5660ceaa11ec82399bbee5ef8fea',
        '_uetvid': 'f1e748b0cd1211ec96b2cdc548e1fd9f',
    }

    headers = {
        'authority': 'redsky.target.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,es;q=0.8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'TealeafAkaSid=waL3jgAdhN0XiguU9qg6d0fJcjwDtucM; visitorId=0180A2D58E740201B23993625ACB1488; sapphire=1; UserLocation=91803|34.070|-118.140|CA|US; egsSessionId=202a9a4a-5cc5-4946-8e08-b5389bc61d05; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI0YWEwZTgwNC0yZGY3LTQyZmQtODUyMy1lOTdjZjZjOTMwOTUiLCJpc3MiOiJNSTYiLCJleHAiOjE2NTIwODU3NDksImlhdCI6MTY1MTk5OTM0OSwianRpIjoiVEdULjNjYzhhYmJjYjg5MDQ2ZDE5ZTg3ZDAwODRjNzc5NWY3LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6Ijc4ZTEzNTdiNjZmZDNmNTllNWM4NWYzOTg4ZjQzNzk5MmMwZmJlYzIxYmFmMDdmMzYyZGI5NTMwNTcxNTRhYmQiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.OlWNDvmAYEm3Wx8fErfOCuxzKmF2Cv-f3LBVrIcgbAVlteuqm6GkbuqEJv49b6j2o8JQoSguPPKV3mErigSVhPBsThZEvLDkxceOaQfBBgPHbn8IP-YxWaXb7zAFiIg9q0FXfqpSjesFNF7eOy7khRiPnFB8Aa0Fmc60mskfEMNwM8I7pUzre1Z_lF5UVB4BeVDWUF2TpMByTHXKmXoLHWzTB410CGEd-hZVkj56c7elVNh7IYyN_H6cWfVyaZje7tQddilZgHbxYfI7dNNPdslr4T-OmWuLRE-XJncyEvOnqtlPjUCXAuURZVMbKgLqoCVSaerc5FkXPiiXP3UaDA; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiI0YWEwZTgwNC0yZGY3LTQyZmQtODUyMy1lOTdjZjZjOTMwOTUiLCJpc3MiOiJNSTYiLCJleHAiOjE2NTIwODU3NDksImlhdCI6MTY1MTk5OTM0OSwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.; refreshToken=uGypaLhlWlWT1bIOtIlfu9GTFXnyyDnT27v8WrGIdmGblmME8mcdCJ615GpjdPjDQVrAdnc_RsTfVXqPcK2C1w; __gpi=UID=000005603bb0d81d:T=1651999349:RT=1651999349:S=ALNI_MZYAjjnoTaXZKNHWTX3uHodjqlSTg; fiatsCookie=DSI_184|DSN_Alhambra|DSZ_91801; _mitata=OWVhZmE2YmY4OGMxMDdhYTI2OTUxM2U1Zjc0MjQxNTAwNTQwMmFjZWQzYjZkZWMyYzA5ODg0NjkxMWViNzJhYQ==_/@#/1651999410_/@#/cCVzrt4ugLvrbBGW_/@#/ZjIxYTkwYzAwY2RlYTNiMGEwYmIwZTM4N2JhNDg3MTJjZWVmNTg2ZGM2YTgwN2JhNjMzYmYzOTc5M2QyM2JmYQ==_/@#/000; ci_pixmgr=other; _gcl_au=1.1.1744745437.1651999352; __gads=ID=279fd1e6d1b46bbc:T=1651999349:S=ALNI_MZl-WphOYuq372ZYWKy5KuSH0_6xw; ffsession={%22sessionHash%22:%221552af6b77b7641651999347791%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=ground+beef&category=0|All|matchallpartial|all%2520categories&tref=typeahead%257Cterm%257Cundefined%257Cground%2520beef%257C%257C%257C%257Cservice%257C%257C%257C%257C&searchTermRaw=groun%22%2C%22sessionHit%22:3%2C%22prevSearchTerm%22:%22ground%20beef%22}; _uetsid=ccac5660ceaa11ec82399bbee5ef8fea; _uetvid=f1e748b0cd1211ec96b2cdc548e1fd9f',
        'origin': 'https://www.target.com',
        'referer': 'https://www.target.com/s?searchTerm=ground+beef&category=0|All|matchallpartial|all%20categories&tref=typeahead%7Cterm%7Cundefined%7Cground%20beef%7C%7C%7C%7Cservice%7C%7C%7C%7C&searchTermRaw=groun',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    }

    params = {
        'key': '9f36aeafbe60771e321a7cc95a78140772ab3e96',
        'channel': 'WEB',
        'count': '24',
        'default_purchasability_filter': 'true',
        'include_sponsored': 'true',
        'keyword': 'ground beef',
        'offset': str(i),
        'page': '/s/ground beef',
        'platform': 'desktop',
        'pricing_store_id': '184',
        'scheduled_delivery_store_id': '1411',
        'store_ids': '184,1411,883,1332,189',
        'useragent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'visitor_id': '0180A2D58E740201B23993625ACB1488',
    }
    # get request to results page
    response = requests.get('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1', params=params,
                            cookies=cookies, headers=headers)
    # create json object
    results_json = response.json()
    # access & save the products into a variable via data keys
    result_items = results_json['data']['search']['products']
    # each items' data is now stored in result_items

    # store each items' name, brand, and price
    for result in result_items:
        # item name
        item_title.append(result['item']['product_description']['title'].replace('- Good &#38; Gather&#8482;', ''))
        # item price
        item_price.append(result['price']['formatted_current_price'])
        # item brand -- if no brand, provide item ID number
        try:
            item_brand.append(result['item']['primary_brand']['name'])  # brand name
        except:
            item_brand.append("ID number: " + result['item']['dpci'])  # ID number

# construct pandas dataframe
groundBeef_df = pd.DataFrame({'item_title':item_title, 'item_brand':item_brand, 'item_price':item_price})
print(groundBeef_df)