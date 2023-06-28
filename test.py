import curses
import time

menu = ['Home', 'Play', 'Scoreboard', 'Exit']
y_or_n = ['yes', 'no']


def print_vertical_menu(SEL_WIN, menu, selected_row_idx):
	
	h, w = SEL_WIN.getmaxyx()
	
	for idx, row in enumerate(menu):
		x = w//2 - len(row)//2
		y = h//2 - len(menu)//2 + idx
		if idx == selected_row_idx:
			SEL_WIN.attron(curses.color_pair(1))
			SEL_WIN.addstr(y, x, row)
			SEL_WIN.attroff(curses.color_pair(1))
		else:
			SEL_WIN.addstr(y, x, row)
	SEL_WIN.refresh()

##함수준비:가로로 메뉴를 만드는 함수
def print_horizontal_menu(SEL_WIN, menu , selected_cul_idx):
	len_of_menu = 0
	ex_menu_len = 0
	h, w = SEL_WIN.getmaxyx()

	for cul in menu:
		len_of_menu += len(cul)
	
	for idx, row in enumerate(menu):
		for cul in menu:
			len_of_menu += len(cul)
		y = h//2 + 1
		ex_menu_len = ex_menu_len + len(row) +2
		x = w//2 - len_of_menu + ex_menu_len 
		
		if idx == selected_cul_idx:
			SEL_WIN.attron(curses.color_pair(1))
			SEL_WIN.addstr(y, x, row)
			SEL_WIN.attroff(curses.color_pair(1))
		else:
			SEL_WIN.addstr(y, x, row)
		len_of_menu = 0
	SEL_WIN.refresh()

##함수준비:정중앙에 원하는 문자를 출력하는 함수
def print_center(SEL_WIN, text):
	
	h, w = SEL_WIN.getmaxyx()
	x = w//2 - len(text)//2
	y = h//2
	SEL_WIN.addstr(y, x, text)
	SEL_WIN.refresh()

##함수준비:파일 검색 함수
def findfile(name, path):
	for dirpath, dirname, finding_name in os.walk(path):
		if name in finding_name:
			return os.path.join(dirpath, name)
	

def main(stdscr):
	# turn off cursor blinking
	curses.curs_set(0)

	# color scheme for selected row
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	# specify the current selected row
	current_row = 0
	current_cul = 0 

	# print the menu
	print_vertical_menu(stdscr, menu ,current_row)

	while 1:
		key = stdscr.getch()

		if key == curses.KEY_UP and current_row > 0:
			current_row -= 1
		elif key == curses.KEY_DOWN and current_row < len(menu)-1:
			current_row += 1
		elif key == curses.KEY_ENTER or key in [10, 13]:
			stdscr.clear()
			print_center(stdscr, "You selected '{}'".format(menu[current_row]))
			stdscr.getch()
			# if user selected last row, exit the program
			if current_row == len(menu)-1:
				break
		stdscr.clear()
		print_vertical_menu(stdscr, menu , current_row)
	
	stdscr.clear()
	print_center(stdscr,"Are you sure you want to exit?")
	print_horizontal_menu(stdscr,y_or_n , current_cul)


	while 1:
		key = stdscr.getch()

		if key == curses.KEY_LEFT and current_cul > 0:
			current_cul -= 1
		elif key == curses.KEY_RIGHT and current_cul < len(y_or_n)-1:
			current_cul += 1
		elif key == curses.KEY_ENTER or key in [10, 13]:
			stdscr.clear()
			print_center(stdscr, "You selected '{}'".format(y_or_n[current_cul]))
			stdscr.getch()
			# if user selected last row, exit the program
			if current_cul == 0:
				break
		
		
		print_center(stdscr,"Are you sure you want to exit?")
		print_horizontal_menu(stdscr, y_or_n , current_cul)


curses.wrapper(main)