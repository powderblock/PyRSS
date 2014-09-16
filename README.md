# PyRSS

PyRSS is a Python based RSS reader built on feedparser. I couldn't find an RSS reader I liked, so I made one.

## Overview
  PyRSS aggregates user provided RSS feeds in one place, while still being pretty easy to use.

## Example Usage
  - Just launch `reader_tk.py` to launch the Tkinter based GUI. Alteratively, `reader.py` offers similar functionality to `reader_tk.py`, but in a command line interface.
  - To get started, click the "+" button in the lower left hand corner of the GUI and add an RSS feed. ([Example feed URL](http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml))

## Credits
PyRSS is created by Caleb Jones ([@porglezomp](https://github.com/porglezomp)) and Blade Nelson([@powderblock](https://github.com/powderblock)).
It uses [feedparser](https://pypi.python.org/pypi/feedparser) to parse RSS feeds and [appdirs](https://pypi.python.org/pypi/appdirs/) to find the user-data-dir to store the list of feeds you're following.
