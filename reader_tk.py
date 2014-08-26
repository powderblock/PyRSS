#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser, os, sys, webbrowser, errno
from Tkinter import *

try: import readline
except: import pyreadline as readline

path = os.path.join(os.path.expanduser('~'), 'sites.txt')

class Program(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        try:
            file = open(path, 'r')
            for line in file:
                site = feedparser.parse(line)
                website = Label(text=line)
                website.pack()
                for i in range(0, 3):
                    buttonName = i
                    buttonName = Button(text=site['entries'][i]['title'], command = lambda i=i: self.callback(site['entries'][i]['link']))
                    buttonName.pack(padx=30, pady=15)
                addRSSButton = Button(text="+", command = self.create_window)
                addRSSButton.pack(side="right")

        except (OSError, IOError) as e:
            if (errno.ENOENT == e.errno): 
                print("No file found at: "+path)
    def callback(self, text): webbrowser.get('windows-default').open(text)
    def create_window(self):
        t = Toplevel(self)
        t.wm_title("Add new RSS feed")

        b = Button(t, text="Add New Feed", command = self.addNewFeed)
        b.pack(side="right")

        global e
        e = Entry(t, width=50)
        e.pack(side="left")
    def addNewFeed(self): print e.get()
if __name__ == "__main__":
    root = Tk()
    root.wm_title("PyRSS")
    main = Program(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
