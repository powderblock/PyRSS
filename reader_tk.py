#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser, os, sys, webbrowser, errno

try: from Tkinter import * # python2
except: from tkinter import * # python3

try: import readline
except: import pyreadline as readline

#Path for saved RSS site feeds.
path = os.path.join(os.path.expanduser('~'), 'sites.txt')

urls = []
urlsFull = []

class Program(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        try:
            # Open sites.txt
            file = open(path, 'r')
            # Go through each line in sites.txt
            for line in file:
                line = line.strip()
                urlsFull.append(line)
                if line not in urls:
                    urls.append(line)
                    # Feed line found in file to feedparser
                    site = feedparser.parse(line)
                    # Create labels for each site gotten out of the file
                    website = Label(text=line)
                    website.pack()
                    # Top three entries from the RSS feed
                    for i in range(0, 3):
                        buttonName = i
                        buttonName = Button(text=site['entries'][i]['title'], command = lambda i=i: self.openSite(site['entries'][i]['link']))
                        buttonName.pack(padx=30, pady=15)
            file.close()
            # Make button for adding RSS feeds to 
            addRSSButton = Button(text="+", command = self.create_window)
            addRSSButton.pack(side="right")

        except (OSError, IOError) as e:
            # Confirm the error type
            if (errno.ENOENT == e.errno):
                # Tell the user the file was not found.
                print("No file found at: "+path)
    def openSite(self, text): webbrowser.get().open(text)

    # Create new window for adding new RSS feed to file.
    def create_window(self):
        t = Toplevel(self)
        t.wm_title("Add new RSS feed")

        newFeedButton = Button(t, text="Add New Feed", command = self.addNewFeed)
        newFeedButton.pack(side="right")

        global newFeedGet
        newFeedGet = Entry(t, width=50)
        newFeedGet.pack(side="left")

    def addNewFeed(self):
        add = open(path, 'w')
        for i in range(0, len(urlsFull)):
            add.write(urlsFull[i])
        add.write("\n"+newFeedGet.get())
        
        
if __name__ == "__main__":
    root = Tk()
    root.wm_title("PyRSS")
    main = Program(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
