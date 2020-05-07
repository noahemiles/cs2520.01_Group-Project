import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



class liveGraph:

	def __init__ (self, stockLabel):
		plt.style.use('ggplot') # style of graph
		self.stockLabel = stockLabel.upper()

	def update(self, i):
		try:
			data = pd.read_csv(f'./csvFiles/{self.stockLabel}.csv', names = ['colA','colB'], header=None) # Update File Path
			x = data['colA'] # Grab data from first column of CSV
			y = data['colB'] # Grab data from second column of csv
			plt.cla()        # clear axis for next graph
			plt.plot(x,y, label = f'{self.stockLabel} Stock') 
			plt.xlabel("Time (PST)")
			plt.ylabel("Value ($)")
			plt.title(f'{self.stockLabel.upper()} Stock')
			plt.legend(loc = 'upper left')
		except Exception as ex:
			print(ex,"Incorrect File Path")

	def graph(self):	
		ani = FuncAnimation(plt.gcf(), self.update, interval=60000)
		plt.tight_layout()
		plt.show()



