import time
from tkinter import *
import liveGraph as g


root = Tk() 
#top = Toplevel() # Creates a new window
# GUI Implementation
root.geometry("800x452")
root.title("Live Stock Graphs")

background_image = PhotoImage(file='stonks.png')
background_label = Label(root, image=background_image)
background_label.pack()

def testing(stockLabel):
	obj1 = g.liveGraph(stockLabel)
	obj1.graph()

frame = Frame(root, bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=.75, relheight=.1, anchor='n')

button = Button(frame, text="Show stock", fg = 'red', command = lambda: testing(entry.get()))
button.place(relx=.75, rely=0, relwidth=.25, relheight=1)

entry = Entry(frame, bg = '#80c1ff')
entry.place(relx=0, rely=0, relwidth=.54, relheight=1)

label = Label(root, bg = 'gray', text="Enter Stock Label Below")
label.place(relx=.125, rely=.05, relwidth=.404, relheight=.05)

#lower_frame = Frame(root, bg='#ccc6ff', bd=10)
#lower_frame.place(relx=0.5, rely=.25, relwidth=.75, relheight=.6, anchor='n')
#
#lower_label = Label(lower_frame, text="Displaying Stock")
#lower_label.place(relwidth=1, relheight=1)



# GUI Implementation Ends
root.mainloop() 
#top.mainloop()

