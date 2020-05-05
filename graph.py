from matplotlib import pyplot as plt
import csv
from datetime import time

class Graph:
	def __plotGraph(self, label, times, values):
		plt.style.use('ggplot')
		plt.plot(times,values, color='k',label = f'{label} Stock Value')
		plt.gcf().autofmt_xdate()
		plt.xlabel("Time (PST)")
		plt.ylabel("Value ($)")
		plt.title(label.upper())
		plt.legend()
		plt.show()

	def checkStock(self, stockLabel):
		try:
			#stockLabel = input("Enter Stock Label: ").upper()
			self.stockLabel = stockLabel.upper()
			self.stockPrices = []
			self.stockTimes = []
			with open('./csvFiles/' + stockLabel + '.csv', newline='') as file:
				reader = csv.reader(file)
				x = 50
				for val in reader:
					if(x%50 == 0):
						self.stockPrices.append(''.join(val[0]))
						self.stockTimes.append(''.join(val[1]))
					x += 1
			self.stockPrices = [x.replace(",","") for x in self.stockPrices]
			self.stockPrices = list(map(float, self.stockPrices))
			self.__plotGraph(self.stockLabel, self.stockTimes, self.stockPrices)

		except FileNotFoundError as e:
			print(e)

