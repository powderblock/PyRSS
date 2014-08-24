#!/usr/bin/python
import feedparser, os, sys

try:
        import readline
except:
        import pyreadline as readline

path = os.path.join(os.path.expanduser('~'), 'sites.txt')

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
    except:
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
#menu()

