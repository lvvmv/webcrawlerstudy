#coding:utf-8
from bs4 import  BeautifulSoup
from urlparse import urljoin
import requests
import csv
import html5lib

URL = "http://wh.ganji.com/fang1/o{page}/_%E5%8D%8E%E4%B8%AD%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6/"
ADDR = "http://wh.ganji.com/"

if __name__ == '__main__':
	start_page  = 1
	end_page =10
	price  = 7
	with open('ganji.csv','wb') as f:
		csv_writer = csv.writer(f,delimiter=',')
		print 'start......'
		while start_page <= end_page:
			print('GET:{0}'.format(URL.format(page = start_page)))
			response = requests.get(URL.format(page = start_page))
			html = BeautifulSoup(response.text,'html.parser')
			house_list = html.select('.f-list > .f-list-item > .f-list-item-wrap')
			# print house_list
			if not house_list:
				break
			for house in house_list:
				print house
				house_title = house.select('.title > a')[0].string.encode('utf-8')
				house_addr = house.select('.address > .area > a')[-1].string.encode('utf-8')
				house_price = house.select('.info > .price > .num')[0].string.encode('utf-8')
				house_url = urljoin(ADDR,house.select('.title > a')[0]['href'])
				csv_writer.writerow([house_title,house_addr,house_price,house_url])
			start_page+=1
	print 'end.....'
