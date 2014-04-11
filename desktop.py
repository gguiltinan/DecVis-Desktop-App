from Tkinter import * 
import sys
import urllib
import urllib2
import json
import settings
import settingsdesktop

class mainWindow(object):
    def __init__(self,master):
        self.master=master
          
	if settingsdesktop.mod1 == True:
		f= Frame(master, bg = "white", width = 250, height = 250)
		f.pack(side=LEFT, expand = 1, pady = 10, padx = 10)
	else:
		f = Frame(master, bg = "black", width = 250, height = 250)
		f.pack(side=LEFT, expand = 1, pady = 10, padx = 10)

	if settingsdesktop.mod2 == True:
		f2 = Frame(master, bg = "white", width = 250, height = 250)
		f2.pack(side=LEFT, expand = 1, pady = 10, padx = 10)
	else:
		f2 = Frame(master, bg = "black", width = 250, height = 250)
		f2.pack(side=LEFT, expand = 1, pady = 10, padx = 10)

	if settingsdesktop.mod3 == True:
		f3 = Frame(master, bg = "white", width = 250, height = 250)
		f3.pack(side=LEFT, expand = 1, pady = 10, padx = 10)
	else:
		f3 = Frame(master, bg = "black", width = 250, height = 250)
		f3.pack(side=LEFT, expand = 1, pady = 10, padx = 10)	
		


if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()