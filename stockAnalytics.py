from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen
from datetime import datetime
import requests
import threading
import time
import csv
import os



class StockAnalytics:
	def __init__(self, stockLabel, timePerPriceCheck = 30, url = "http://www.finance.yahoo.com/quote/"):
		self.stockLabel = stockLabel.upper()
		self.timePerPriceCheck = timePerPriceCheck #seconds
		self.url = url + stockLabel.upper()

	def getStockLabel(self):
		return self.stockLabel

	def getUrl(self):
		return self.url

	def getPage(self):
		return requests.get(self.url).text

	def getStockPrice(self):
		return bsoup(self.getPage(),"html.parser").find('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').get_text()

	def writeCSVFile(self):
		try:
			stockLabelFile = csv.writer(open('./csvFiles/' + self.getStockLabel() + ".csv", "a"))
		except IOError as err:
			os.mkdir("./csvFiles")
			stockLabelFile = csv.writer(open('./csvFiles/' + self.getStockLabel() + ".csv", "a"))
		except Exception as ex:
			print(ex)
			return False
		finally:
			today = datetime.now()
			dt_string = today.strftime("%H:%M")
			year = today.year
			month = today.month
			day = today.day
			stockLabelFile.writerow([self.getStockPrice(), dt_string, month, day, year])
		return True

	def collectStockPrices(self, totalTime, timeUnit = "H"):
		if timeUnit.upper() is "S":
			endTime = time.time() + totalTime
		elif timeUnit.upper() is "M":
			endTime = time.time() + 60 * totalTime
		else:
			endTime = time.time() + 3600 * totalTime
		while(time.time() < endTime):
			time.sleep(self.timePerPriceCheck)
			self.writeCSVFile()

	def __str__(self):
		return self.getStockLabel() + ": " + self.getStockPrice()

def dayCollection():
	print("Starting collection:", datetime.now())
	StockList = list()
	StockList.append(StockAnalytics("F"))
	StockList.append(StockAnalytics("AMZN"))
	StockList.append(StockAnalytics("NFLX"))
	StockList.append(StockAnalytics("GOOG"))
	StockList.append(StockAnalytics("AAPL"))
	StockList.append(StockAnalytics("TSLA"))
	StockList.append(StockAnalytics("CVX"))

	threadList = list()
	for stock in StockList:
		thread = threading.Thread(target=stock.collectStockPrices, args = (7,"H"))
		threadList.append(thread)
		thread.start()

def autoStart():	
	current_time = datetime.today()
	timeToStart = current_time.replace(day=current_time.day+1,hour=6,minute=15,second=0,microsecond=0)
	delta_t = timeToStart - current_time
	secs = delta_t.seconds+1
	waitThread = threading.Timer(secs,dayCollection)
	waitThread.start()

def main():
	autoStart()


if __name__ == '__main__':
	main()

'''
tests:

if TSLA.writeCSVFile():
	print("File Write Success")
else:
	print("File Write Fail")

'''
'''
print(StockAnalytics("TSLA"))
print(StockAnalytics("DIS"))
print(StockAnalytics("CVX"))
print(StockAnalytics("MSFT"))

	
'''