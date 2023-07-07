import curses
import time
import os
import os.path
import time
import getpass
import sys

##자료준비
##자료준비:로고 큰거
logo_big = [
'⠀⠀⠀⠀⠀⠀⢀⡠⠔⠊⡟⠲⢤⣀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⢀⣠⣄⣀⢸⠀⠀⠀⡇⠀⠀⢸⠀⣀⣄⣀⠀⠀⠀',
'⡴⠚⠁⢸⣿⣿⣿⠀⠀⠀⡇⠀⠀⢸⡿⠋⠀⠈⠙⣢⠄',
'⡇⠀⠀⢸⡿⠟⠋⠀⠀⠀⡇⠀⠀⠈⠀⠀⠀⢀⡼⠁⠀',
'⡇⠀⠀⠈⠀⠀⣀⠀⠀⠀⡇⠀⠀⢰⠀⠀⠠⡎⠀⠀⠀',
'⡇⠀⠀⢠⣶⣿⣿⠀⠀⠀⡇⠀⠀⢸⣧⠀⠀⢳⡀⠀⠀',
'⡇⠀⠀⢸⣿⣿⣿⣀⠤⠖⠓⠦⣀⣸⣿⣆⠀⠀⢳⠀⠀',
'⡇⠀⠀⢸⣿⣿⣿⣤⣀⠀⠀⢀⣤⣿⣿⣿⣆⠀⠀⢧⠀',
'⡧⠔⠋⠁⠈⠛⠻⣿⠀⠉⠋⠀⢻⣿⠿⠋⠁⠉⠓⠬⣇',
'⠉⠐⠦⣀⡠⠔⠊⠁⠀⠀⠀⠀⠀⠉⠒⠦⣄⡠⠔⠊⠉']

##자료준비:시작화면 메뉴
start_screen_menu = ['','Turn off']

##자료준비:yes or no
y_or_n = ['Yes','No']

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
	##화면의 최대 사이즈를 먼저 조사
	stdscr_hight, stdscr_width = stdscr.getmaxyx()
	half_hight, half_width = stdscr_hight//2 , stdscr_width//2

	##화면에 먼저 로고를 그리고 메뉴를 로고 우측에 생성, 아래에 선택화면 그리기
	stdscr.clear()
	drew_ASCIIart(stdscr, logo_big, half_hight, half_width - len(logo_big[0])//2-5)
	menu_vertical_1(stdscr, start_screen_info, 99, half_hight, half_width + len(start_screen_info[0])//2+5)
	menu_horizontal(stdscr, y_or_n, 0, half_hight + len(logo_big)//2 + 3 , half_width)
	stdscr.addstr(half_hight + len(logo_big)//2 + 1, half_width - len("Do you want to start OGA_PMTE?")//2, "Do you want to start OGA_PMTE?")
	stdscr.refresh()

	##시작할지 말지를 선택하는 메뉴를 작동
	selected_column = 0
	turnoff_menu_select = 0

	while True:
		key = stdscr.getch()
		if key == curses.KEY_LEFT and selected_column > 0:
			selected_column = 0
		elif key == curses.KEY_RIGHT and selected_column < 1:
			selected_column = 1
		elif key == curses.KEY_ENTER or key in [10, 13]:
			 ##Yes를 선택할 경우 MAIN_MENU를 실행
			if selected_column == 0:
				os.system("python MAIN_MENU.py")
				break
			 ##No를 선택하는 경우 다시한번 물어보기
			elif selected_column == 1:
				stdscr.clear()
				stdscr.addstr(half_hight-1, half_width-len("Do you want to turn off the device?")//2, "Do you want to turn off the device?")
				menu_horizontal(stdscr, ['Turn off', 'No'], turnoff_menu_select,half_hight+1, half_width)
				stdscr.refresh()
				while True:
					key = stdscr.getch()				
					if key == curses.KEY_LEFT and turnoff_menu_select > 0:
						turnoff_menu_select = 0
					elif key == curses.KEY_RIGHT and turnoff_menu_select < 1:
						turnoff_menu_select = 1
					elif key == curses.KEY_ENTER or key in [10, 13]:
						 ##Turn off를 선택한 경우 시스템을 종료
						if turnoff_menu_select == 0:
							stdscr.clear()
							os.system("sudo shutdown now")
							sys.exit()
						 ##No를 선택한 경우에는 다시 작동할지말지 선택하는 메뉴로 복귀
						elif turnoff_menu_select == 1:
							turnoff_menu_select = 0
							break
					stdscr.clear()
					stdscr.addstr(half_hight-1, half_width-len("Do you want to turn off the device?")//2, "Do you want to turn off the device?")
					menu_horizontal(stdscr, ['Turn off', 'No'], turnoff_menu_select,half_hight+1, half_width)
					stdscr.refresh()
			if turnoff_menu_select == 1:
				stdscr.clear()
				break  
		
		stdscr.clear()
		drew_ASCIIart(stdscr, logo_big, half_hight, half_width - len(logo_big[0])//2-5)
		menu_vertical_1(stdscr, start_screen_info, 99, half_hight, half_width + len(start_screen_info[0])//2+5)
		menu_horizontal(stdscr, y_or_n, selected_column, half_hight + len(logo_big)//2 + 3 , half_width)
		stdscr.addstr(half_hight + len(logo_big)//2 + 1, half_width - len("Do you want to start OGA_PMTE?")//2, "Do you want to start OGA_PMTE?")
		stdscr.refresh()

	stdscr.clear()
	stdscr.refresh()
	time.sleep(3)
		
			

curses.wrapper(main)