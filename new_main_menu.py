import curses
import time
import os
import os.path
import time
import getpass
import sys

##자료준비
##자료준비: 메인 메뉴
Main_menu = []

##자료준비:시스템 정보
USER = getpass.getuser()
DATE = str(time.strftime('%Y-%m-%d'))
RAW_INFO = os.uname()
Architecture_INFO = RAW_INFO[4]
OS_INFO = RAW_INFO[3].split(" ")   
INFO_FILE = open('info.txt')
VERS,UPDATE = INFO_FILE.read().split("\n")
INFO_FILE.close()
start_screen_info = [f'USER : {USER}', DATE, VERS, UPDATE, f"{Architecture_INFO} {OS_INFO[0]}"]


##설정준비
##설정준비:색상설정
curses.initscr()
curses.start_color()

curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)	 
curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)
curses.init_pair(3,curses.COLOR_CYAN,curses.COLOR_WHITE)

MAIN_COLOR = curses.color_pair(1)
MAIN_COLOR_REVERSE = curses.color_pair(2)
SELECT_COLOR = curses.color_pair(3)

##설정준비:커서 색상 설정
curses.curs_set(0)


##그리기함수
##그리기함수:세로로 메뉴를 나열
def menu_vertical(selected_window, menu_item, selected_row, middle_hight, middle_width):
	for index, item in enumerate(menu_item):
		item_x = middle_width - len(item)//2
		item_y = middle_hight - len(menu_item)//2 + index
	
		if index == selected_row:
			selected_window.addstr(item_y, item_x, item, SELECT_COLOR)
		else:
			selected_window.addstr(item_y, item_x, item)
	selected_window.refresh()

##그리기함수:세로로 메뉴를 나열(한줄 건너 하나)
def menu_vertical_1(selected_window, menu_item, selected_row, middle_hight, middle_width):
	for index, item in enumerate(menu_item):
		item_x = middle_width - len(item)//2
		item_y = middle_hight - len(menu_item) + index * 2
	
		if index == selected_row:
			selected_window.addstr(item_y, item_x, item, SELECT_COLOR)
		else:
			selected_window.addstr(item_y, item_x, item)
	selected_window.refresh()


##그리기함수:가로로 메뉴를 나열
def menu_horizontal(selected_window, menu_item, selected_column, middle_hight, middle_width):
	item_x = middle_width

	for item in menu_item:
		
		item_x -= (len(item)+2)//2

	for index, item in enumerate(menu_item):
		item_y = middle_hight

		if index == selected_column:
			selected_window.addstr(item_y, item_x, item, SELECT_COLOR)
		else:
			selected_window.addstr(item_y, item_x, item)
		
		item_x += len(item) + 2
	selected_window.refresh()

##그리기함수:아스키아트를 그림
def drew_ASCIIart(selected_window, art, middle_hight, middle_width):
	for index, item in enumerate(art):
		item_x = middle_width - len(item)//2
		item_y = middle_hight - len(art)//2 + index
		selected_window.addstr(item_y, item_x, item)
	selected_window.refresh()


##기능함수
##기능함수:창 또는 화면의 사이즈를 조사
def maxyx(selected_window):
	max_hight, max_width = selected_window.getmaxyx()
	return max_hight, max_width 



##메인
def main(stdscr):
	##먼저 화면의 사이즈를 조사하고 분할하기
	max_hight, max_width = maxyx(stdscr)
	
	top_screen_hight , top_screen_width = 0, max_width
	bot_screen_hight , bot_screen_width = max_hight-1, max_width

	
	

curses.wrapper(main)