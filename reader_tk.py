#!/usr/bin/python
import feedparser, os, sys, webbrowser
from Tkinter import *

try: import readline
except: import pyreadline as readline

path = os.path.join(os.path.expanduser('~'), 'sites.txt')

def callback(text): webbrowser.get('windows-default').open(text)

root = Tk()

root.wm_title("PyRSS")

class Program:
    def __init__(self):
        try:
            file = open(path, 'r')
            print("File found at "+path)
            for line in file:
                site = {'name:': 'foo', 'site': line};
                site = feedparser.parse(site['site'])
                website = Button(text=line)
                website.pack()
                for i in range(0, 5):
                    buttonName = "button"+line
                    buttonName = Button(text=site['entries'][i]['title'], command = lambda: callback(site['entries'][i]['link']))
                    buttonName.pack(padx=30, pady=15)
            file.close()
        except: print("No file found at "+path)

program = Program()
mainloop()

