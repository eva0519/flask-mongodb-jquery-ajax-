import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

# print(rjson)

rows = rjson['RealtimeCityAir']['row']

print(rows)

for row in rows:
    gu_name = row['MSRSTE_NM']
    gu_mise = row['IDEX_MVL']
    if gu_mise < 60:
        print(gu_name, ":", gu_mise)
