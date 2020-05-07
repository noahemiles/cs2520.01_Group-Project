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
	'''
	Sets stock label, the time interval to check stock price, and the url of the webpage
	'''
		self.stockLabel = stockLabel.upper()
		self.timePerPriceCheck = timePerPriceCheck #seconds
		self.url = url + stockLabel.upper()

	def getStockLabel(self):

	'''
	Returns the stock label 
	'''
		return self.stockLabel

	def getUrl(self):
	'''
	Returns the url of the webpage
	'''
		return self.url

	def getPage(self):
	'''
	Returns the webpage text of the url
	'''
		return requests.get(self.url).text

	def getStockPrice(self):
	'''
	Parses the webpage for the stock price 
	'''
		return bsoup(self.getPage(),"html.parser").find('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').get_text()

	def writeCSVFile(self):
	'''
	Writes stock information to csv file
	'''
		try:
			stockLabelFile = csv.writer(open('./csvFiles/' + self.getStockLabel() + ".csv", "a"))
		except IOError as err:
			#creates csvFile directory if one does not exist in the current directory
			os.mkdir("./csvFiles")
			stockLabelFile = csv.writer(open('./csvFiles/' + self.getStockLabel() + ".csv", "a"))
		except Exception as ex:
			print(ex)
			return False
		finally:
			#time information
			today = datetime.now()
			dt_string = today.strftime("%H:%M")
			year = today.year
			month = today.month
			day = today.day
			try:
				#file write row
				stockLabelFile.writerow([self.getStockPrice(), dt_string, month, day, year])
			except AttributeError as writeError:
				return False
		return True


	def collectStockPrices(self, totalTime, timeUnit = "H"):
	'''
	Controls how long it is to write to the csv file

	Default time unit is HOURS
	'''
		if timeUnit.upper() is "S":
			endTime = time.time() + totalTime
		elif timeUnit.upper() is "M":
			endTime = time.time() + 60 * totalTime
		else:
			endTime = time.time() + 3600 * totalTime
		while(time.time() < endTime):
			time.sleep(self.timePerPriceCheck)
			if not self.writeCSVFile():
				print("Error Writing:",self.getStockLabel(),"|",datetime.now())

	def __str__(self):
	'''
	@Override 
	Prints Stock Label : Stock Price
	'''
		return self.getStockLabel() + ": " + self.getStockPrice()


def dayCollection():
	'''
	Collects stock data from all stock labels in StockList for 7 hours by default
	'''
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Starting collection:", datetime.now())
	StockList = list()
	StockList.append(StockAnalytics("DIS"))
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
	try:
		timeToStart = current_time.replace(day=current_time.day+1,hour=6,minute=15,second=0,microsecond=0)
	except ValueError as newMonth:
		timeToStart = current_time.replace(month=current_time.month+1,day=1,hour=6,minute=15,second=0,microsecond=0)
	delta_t = timeToStart - current_time
	secs = delta_t.seconds+1
	waitThread = threading.Timer(secs,dayCollection)
	waitThread.start()

def main():
	#manual start meaning, starting immediately 
	#auto start meaning, starting the next day at 6am
	if input("Manual Start = 0\nAuto Start = 1\n\tInput: ") is 0:
		dayCollection()
	else:
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