#!/usr/bin/env python
#imports
import urllib
import sys
import curses

#initialise curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)

#create gui structure
stdscr.addstr("My simple web browser", curses.A_REVERSE)
stdscr.chgat(-1, curses.A_REVERSE)
stdscr.addstr(curses.LINES-1, 0, "Press 'q' to quit the browser!")

browser_window = curses.newwin(curses.LINES-2, curses.COLS, 1,0)
browser_text_window = browser_window.subwin(curses.LINES-6,curses.COLS-4, 3,2)
browser_window.box()

#create list to hold links
links = []

#function called when closing, to return terminal to original state
def close():
  curses.nocbreak()
  curses.echo()
  curses.curs_set(1)
  curses.endwin()

#main function that displays pages
def main(currentLink):
  
  #navigation only possible in this url, will improve in future
  url = "http://studentnet.cs.manchester.ac.uk/ugt/COMP18112/" + str(currentLink) +".html"
  
  #split html into individual tokens
  data = urllib.urlopen(url)
  tokens = data.read().split()

  #empty list if links
  del links[:]
  
  #for each token do the appropriate action
  #could be condensed with logical connectives
  for token in tokens:
    if token == '<html>':
      pass
    elif token == '</html>':
      pass
    elif token == '<head>':
      pass
    elif token == '</head>':
      pass
    elif token == '<body>':
      pass
    elif token == '</body>':
      pass
    elif token == '<title>':
      browser_text_window.addstr('Page Title : ')
      title = 1
    elif token == '</title>':
      title = 0
    elif token == '<h1>':
      browser_text_window.addstr('\nHEADING : ')
      h1 = 1
    elif token == '</h1>':
      h1 = 0
    elif token == '<p>':
      browser_text_window.addstr('\n')
      p = 1
    elif token == '</p>':
      p = 0
      browser_text_window.addstr('\n')
    elif token == '<em>':
      pass
    elif token == '</em>':
      pass
    elif token == 'href="./page3.html">':
      links.append('page3')
    elif token == 'href="./page4.html">':
      links.append('page4')
    elif token == 'href="./page5.html">':
      links.append('page5')
    elif token == '</a>':
      pass
    elif token == '<a':
      pass
    else:
      browser_text_window.addstr(' ' + token)

  #initialise index at 1, then print out all found links in order
  index = 1
  browser_text_window.addstr('\nThese are the links from this page! Press the number to go to any of them!')
  for link in links:
    browser_text_window.addstr('\n' + str(index) + ' : ./' + str(link) + ".html")
    index += 1

#initially call the main function
thisLink = 'page3'
main(currentLink = thisLink)

#refresh gui
stdscr.noutrefresh()
browser_window.noutrefresh()

curses.doupdate()

#listen for input and behave accordingly
while True:
  c = browser_window.getch()
  if c == ord('q'):
    close() 
    sys.exit()#
  #check if input is a valid number that isn't larger than the length of
  #the list
  if(c <= 57 and c >= 48):
    if (int(unichr(c)) <= len(links) and int(unichr(c)) > 0):
      browser_text_window.clear()
      main(currentLink = links[int(unichr(c)) - 1])
      stdscr.noutrefresh()
      browser_window.noutrefresh()
      browser_text_window.noutrefresh()
      curses.doupdate()
  else:
    pass

