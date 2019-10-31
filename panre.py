# -*- coding:utf-8 -*-
import requests
import xmltodict
import chardet
import collections


param2 = 3
keyword = '자동차'


raw_data = requests.get(
    f'http://openapi.ccourt.go.kr/openapi/services/PrecedentSearchSvc/getPrcdntSearchInfo?ServiceKey=PgwbRmIwJL%2BKZTXceW%2Bygt2h%2B809EQBIHtvWDvNGPorpmyeSin5SeT1NcJv4B8XLHAJscP0RwwRXOc7uAUdKmg%3D%3D&pansiMatt={keyword}&panreType=0{param2}').content

xmlObject = xmltodict.parse(raw_data)
# for k in range(0, 100):

number_list = []
for i in range(0, len(xmlObject['response']['body']['items']['item'])):
    number = xmlObject['response']['body']['items']['item'][i]['eventNum']
    print(number)
    number_list.append(number)
for k in number_list:
    raw_data2 = requests.get(
        f'http://openapi.ccourt.go.kr/openapi/services/PrecedentSearchSvc/getPrcdntDetailInfo?ServiceKey=aSsGKoThyf2YjJ+v57ZJWnxgD0OMKY4iKjUMCg/RlngOziGK1mkHcB7hVIqlnyJoYVbbOS7fgvU2S7WAAhL1fA==&eventNum={k}&panreType=0{param2}').content

xmlObject = xmltodict.parse(raw_data2)

a = xmlObject['response']['body']['items']['item']['pansiMatt']

print(a)
