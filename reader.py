#!/usr/bin/python
import feedparser
import os
import sys
import errno
import appdirs

appname = "PyRSS"
appauthor = "Adventurous"

# If the data directory doesn't exist, create it
datadir = appdirs.user_data_dir(appname, appauthor)
if (not os.path.isdir(datadir)):
    os.makedirs(datadir)
# Path for saved RSS site feeds
path = os.path.join(datadir, "sites.txt")

text = []
# URLs list is mostly used for checking to make sure we aren't showing the same feed twice (or more.)
urls = []

def showRSS():
    # Open sites.txt
    try:
        with open(path, 'r') as f:
            # Get rid of all the newlines while you're reading it in
            text = [x.strip() for x in f.readlines()]
    except:
        pass
    for line in text:
        line = line.strip()
        # we don't want to process the same URL more than once
        if line in urls:
            continue

        urls.append(line)
        # Feed line found in file to feedparser
        site = feedparser.parse(line)
        # Show the URL you are displaying entries from
        print(line)

        num = min(3, len(site['entries']))
        # Top three entries from the RSS feed
        for entry in site['entries'][:num]:
            title = entry['title']
            link = entry['link']
            print(title)
            print(link)
        print("No more entries!\n")

def addNewFeed():
    global text
    # Open the file for appending and just write the new line to it
    new = raw_input("Enter RSS feed to add: ")
    # If you're not subscribed already, subscribe!
    if (new not in text):
        text.append(new)
        with open(path, 'a') as f:
            f.write(new + "\n")
    showRSS()

def menu():
    while True:
        choice = raw_input("1.Show RSS feeds\n2.Add new RSS feed\n")
        if choice == "1": showRSS(); break

        elif choice == "2": addNewFeed(); break

        else: print("\n~That is not a valid option!~")

menu()
