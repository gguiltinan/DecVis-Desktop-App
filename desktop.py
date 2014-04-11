from Tkinter import * 
import sys
import urllib
import urllib2
import json
import settings
import settingsdesktop


class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Enter username")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.l1=Label(top,text="Enter password")
        self.l1.pack()
        self.e1=Entry(top)
        self.e1.pack()
        self.b=Button(top,text='Login',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.username=self.e.get()
        self.password=self.e1.get()
        with open('desktopsettings.json', 'w') as fp:
            json.dumps({'username': self.username}, fp)
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=Button(master,text="Login",command=self.popup)
        self.b.pack()
        self.b2=Button(master,text="print value",command=lambda: sys.stdout.write(self.userName()+'\n'+self.password()))
        self.b2.pack()
          
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
		

    def popup(self):
        self.w=popupWindow(self.master)
        self.master.wait_window(self.w.top)

    def userName(self):
		return self.w.username
        
    def password(self):
        return self.w.password

if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()