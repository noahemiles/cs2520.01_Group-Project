from matplotlib import pyplot as plt
import csv
from datetime import time


def plotGraph(times, values):
	plt.plot(stockTimes,stockPrices)
	plt.xlabel("Time (PST)")
	plt.ylabel("Value ($)")
	plt.title(stockLabel.upper())
	plt.legend(['Apple Stock Value'])
	plt.show()


try:
	stockLabel = input("Enter Stock Label: ").upper()
	stockPrices = []
	stockTimes = []
	with open('./csvFiles/' + stockLabel + '.csv', newline='') as file:
		reader = csv.reader(file)
		for val in reader:
			stockPrices.append(''.join(val[0]))
			stockTimes.append(''.join(val[1]))

	stockPrices = [x.replace(",","") for x in stockPrices]
	stockPrices = list(map(float, stockPrices))
	plotGraph(stockTimes, stockPrices)

except FileNotFoundError as e:
	print(e)