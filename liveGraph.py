import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



class liveGraph:
	def __init__ (self, stockLabel):
		plt.style.use('ggplot')
		self.x_vals = []
		self.y_vals = []
		self.stockLabel = stockLabel.upper()

	def update(self, i):
		try:
			data = pd.read_csv(f'./{self.stockLabel}.csv') # Update File Path
			x = data['x_value']
			y = data['total_1']
			plt.cla() # clear axis
			plt.plot(x,y, label = f'{self.stockLabel} Stock') 
			plt.xlabel("Time (PST)")
			plt.ylabel("Value ($)")
			plt.title(f'{self.stockLabel.upper()} Stock')
			plt.legend(loc = 'upper left')
		except Exception as ex:
			print(ex,"Incorrect File Path")

	def graph(self):	
		ani = FuncAnimation(plt.gcf(), self.update, interval=1000)
		plt.tight_layout()
		plt.show()

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

obj1 = liveGraph('tsla')
obj1.graph()

