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
buttons = []

root = Tk()
root.wm_title("PyRSS")

try:
    # Open sites.txt
    file = open(path, 'r')
    # Go through each line in sites.txt
    for line in file:
        line = line.strip()
        if line not in urls:
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
            # When we're read all the entries, inform the user
            noMoreEntries = Label(root, text="No more entries!")
            noMoreEntries.pack(padx=5, pady=5)
    file.close()
    # Make button for adding RSS feeds to 
    addRSSButton = Button(root, text="+", command=lambda: create_window())
    addRSSButton.pack(side="right")

except (OSError, IOError) as e:
    # Confirm the error type
    if (errno.ENOENT == e.errno):
        # Tell the user the file was not found.
        print("No file found at: " + path)

def openSite(text): webbrowser.get().open(text)

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
    # Open the file for appending and add the new line to it
    with open(path, 'a') as add:
        add.write(newFeedGet.get() + "\n")
        feed.destroy()

root.mainloop()
