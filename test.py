import curses

menu = ['Home', 'Play', 'Scoreboard', 'Exit']
y_or_n = ['yes', 'no']


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
    	x = w//2 - len(row)//2
    	y = h//2 - len(menu)//2 + idx
    	if idx == selected_row_idx:
    		stdscr.attron(curses.color_pair(1))
    		stdscr.addstr(y, x, row)
    		stdscr.attroff(curses.color_pair(1))
    	else:
    		stdscr.addstr(y, x, row)
    stdscr.refresh()

def print_x_menu(stdscr, selected_cul_idx):
    al = 0
    ex = 0
    h, w = stdscr.getmaxyx()

    for cul in y_or_n:
    	al = al + len(cul)
        
    for idx, row in enumerate(y_or_n):
    	for cul in y_or_n:
    		al = al + len(cul)
    	y = h//2 + 1
    	ex = ex + len(row) +2
    	x = w//2 - al + ex 
    	
    	if idx == selected_cul_idx:
    		stdscr.attron(curses.color_pair(1))
    		stdscr.addstr(y, x, row)
    		stdscr.attroff(curses.color_pair(1))
    	else:
    		stdscr.addstr(y, x, row)
    	al = 0
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0
    current_cul = 0 

    # print the menu
    print_menu(stdscr, current_row)

    while 1:
    	key = stdscr.getch()

    	if key == curses.KEY_UP and current_row > 0:
    		current_row -= 1
    	elif key == curses.KEY_DOWN and current_row < len(menu)-1:
    		current_row += 1
    	elif key == curses.KEY_ENTER or key in [10, 13]:
    		print_center(stdscr, "You selected '{}'".format(menu[current_row]))
    		stdscr.getch()
    		# if user selected last row, exit the program
    		if current_row == len(menu)-1:
    			break

    	print_menu(stdscr, current_row)
	
    stdscr.clear()
    print_center(stdscr,"Are you sure you want to exit?")
    print_x_menu(stdscr,current_cul)

    while 1:
    	key = stdscr.getch()

    	if key == curses.KEY_LEFT and current_cul > 0:
    		current_cul -= 1
    	elif key == curses.KEY_RIGHT and current_cul < len(y_or_n)-1:
    		current_cul += 1
    	elif key == curses.KEY_ENTER or key in [10, 13]:
    		print_center(stdscr, "You selected '{}'".format(y_or_n[current_cul]))
    		stdscr.getch()
    		# if user selected last row, exit the program
    		if current_cul == 0:
    			break

    	print_center(stdscr,"Are you sure you want to exit?")
    	print_x_menu(stdscr, current_cul)

curses.wrapper(main)