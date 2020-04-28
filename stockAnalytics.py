from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen
from datetime import datetime
import threading
import time
import csv
import os



class StockAnalytics:
	def __init__(self, stockLabel, timePerPriceCheck = 5, url = "http://www.finance.yahoo.com/quote/"):
		self.stockLabel = stockLabel.upper()
		self.timePerPriceCheck = timePerPriceCheck #seconds
		self.url = url + stockLabel.upper()

	def getStockLabel(self):
		return self.stockLabel

	def getUrl(self):
		return self.url

	def getPage(self):
		return urlopen(self.url)

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

	def collectStockPrices(self, totalTime, timeUnit = "S"):
		if timeUnit.upper() is "M":
			endTime = time.time() + 60 * totalTime
		elif timeUnit.upper() is "H":
			endTime = time.time() + 3600 * totalTime
		else:
			endTime = time.time() + totalTime
		while(time.time() < endTime):
			time.sleep(self.timePerPriceCheck)
			self.writeCSVFile()

	def __str__(self):
		return self.getStockPrice()

def main():

	TSLA = StockAnalytics("TSLA")
	DIS = StockAnalytics("DIS")

	thread1 = threading.Thread(target=TSLA.collectStockPrices, args=(30,))
	thread2 = threading.Thread(target=DIS.collectStockPrices, args=(30,))
	
	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

if __name__ == '__main__':
	main()

'''
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