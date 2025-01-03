import requests

# @link:https://developers.kakao.com/docs/latest/ko/rest-api/reference#rest-api-list-local
def get_coordinates(address):
    address = address.strip()
    url = "https://dapi.kakao.com/v2/local/search/address.json?query=" + address

    payload = {}
    headers = {
      'Authorization': 'KakaoAK a467bd843cd3482f582ae0b88fca34b5'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # JSON 결과를 파싱하여 'x'와 'y' 좌표 반환
    result = response.json()
    if result['documents']:
        # road_address
        if result['documents'][0]['address'] is None:
            address_info = result['documents'][0]['road_address']
        else:
            address_info = result['documents'][0]['address']

        lon = address_info['x']
        lat = address_info['y']
        return lon, lat
    else:
        print("주소를 찾을 수 없습니다.", address)
        return None, None

def search_apt_query(df):
    return df['시군구'] +  " " + df['번지']