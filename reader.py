import feedparser, os, sys

try:
        import readline
except:
        import pyreadline as readline

path = os.path.join(os.path.expanduser('~'), '.sites')

rss = feedparser.parse('http://rss.cnn.com/rss/cnn_topstories.rss')

def showRSS():
    try:
            file = open(path, 'r')
            print("File found at "+path)
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

menu()
#print(rss['entries'][0]['title'])
