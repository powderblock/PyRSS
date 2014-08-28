#!/usr/bin/python
import feedparser
import os
import sys
import errno

try:
    import readline
except:
    import pyreadline as readline

import appdirs

appname = "PyRSS"
appauthor = "Adventurous"

# If the data directory doesn't exist, create it
datadir = appdirs.user_data_dir(appname, appauthor)
if (not os.path.isdir(datadir)):
    os.makedirs(datadir)
# Path for saved RSS site feeds
path = os.path.join(datadir, "sites.txt")

def showRSS():
    try:
        file = open(path, 'r')
        print("File found at "+path)
        for line in file:
            site = {'name:': 'foo', 'site': line};
            site = feedparser.parse(site['site'])
            print(line)
            for i in range(0, 3):
                    print(site['entries'][i]['title'])

            print("\n")
        file.close()
    except FileNotFoundError:
        print("No file found at "+path)

def addRSS():
    print("You pressed two!")

def liveRSS():
    print("You pressed three!")

def menu():
    while True:
        choice = raw_input("1.Show RSS feeds\n2.Add new RSS feed\n3.Live view RSS feed\n")
        if choice == "1": showRSS(); break

        elif choice == "2": addRSS(); break

        elif choice == "3": liveRSS(); break

        else: print("\n~That is not a valid option!~")

showRSS()
