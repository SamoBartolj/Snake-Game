import curses

#setup window
curess.initscr()
win = curess.newwin(20, 60, 0, 0) #y,x
win.keypad(1)
curses.noecho()
curess.curs_set(0)
win.border(0)
win.nodelay(1)


