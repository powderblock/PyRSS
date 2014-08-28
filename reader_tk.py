#!/usr/bin/python
import feedparser
import os
import sys
import webbrowser
import errno

try: from Tkinter import * # python2
except: from tkinter import * # python3

import appdirs


#Path for saved RSS site feeds.
path = os.path.join(os.path.expanduser('~'), 'sites.txt')

urls = []
buttons = []
text = []

root = Tk()
root.wm_title("PyRSS")

# Open sites.txt
try:
    with open(path, 'r') as f:
        text = f.readlines()
except: pass

# Go through each line in sites.txt
for line in text:
    line = line.strip()
    # we don't want to process the same URL more than once
    if line in urls: continue

    urls.append(line)
    # Feed line found in file to feedparser
    site = feedparser.parse(line)
    # Create labels for each site gotten out of the file
    website = Label(root, text=line)
    website.pack()

    num = min(3, len(site['entries']))
    # Top three entries from the RSS feed
    for entry in site['entries'][:num]:
        title = entry['title']
        callback = lambda link=entry['link']: openSite(link)
        buttons.append(Button(root, text=title, command=callback))
        buttons[-1].pack(padx=30, pady=15)
    noMoreEntries = Label(root, text="No more entries!")
    noMoreEntries.pack(padx=5, pady=5)

# Make button for adding RSS feeds to 
addRSSButton = Button(root, text="+", command=lambda: create_window())
addRSSButton.pack(side="right")

def openSite(text): 
    webbrowser.get().open(text)

# Create new window for adding new RSS feed to file.
def create_window():
    global feed
    feed = Toplevel()
    feed.wm_title("Add new RSS feed")

    newFeedButton = Button(feed, text="Add New Feed", command=lambda: addNewFeed())
    newFeedButton.pack(side="right")

    global newFeedGet
    newFeedGet = Entry(feed, width=50)
    newFeedGet.pack(side="left")

def addNewFeed():
    # Open the file for appending and just write the new line to it
    with open(path, 'a') as f:
        f.write(newFeedGet.get() + "\n")
        feed.destroy()

root.mainloop()
