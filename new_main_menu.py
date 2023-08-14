import curses
import time
import os
import os.path
import time
import getpass
import sys

##자료준비
##자료준비:전체메뉴
Main_menu = {
	'Module' : {'WORKING':':('} , 
	'Commuication' : {
		'I2C' : 'Use pin#7 (GPIO0_C2) as SCL and pin#8 (GPIO0_C3) as SDA to coummuicate with I2C device.',
		'UART' : 'Use UART port at the right side of the device to coummuicate with UART',
		'WIFI' : 'If you are using OGA_Revision_1.1 config WIFI here'
		},
	'GPIO_MENU' : {
		'INPUT_setting' : 'Show input on GPIO pin',
		'OUTPUT_setting' : 'Set GPIO to make output signal',
		'PIN_MAP' : 'Show OGA GPIO pinmap'
		},
	'Setting' : {
		'time_setting' : 'Set time and date',
		'Device_setting' : 'Set power and screen and more...',
		'System_setting' : 'Set OGA_PMTE basic setting'}
}

##자료준비:해골juice
juice = [
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠴⠶⠲⠦⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠉⠀⠀⠀⠀⠀⠀⢀⣀⡁⠤⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⢀⣀⠤⠔⠒⠊⠉⠁⠀⠀⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣮⠤⠔⠚⢫⢠⢢⠀⠀⠀⢀⣠⠤⠐⠚⠉⠁⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡁⢀⢁⢃⢃⣃⠦⠤⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡴⠚⠉⠉⠀⡄⠀⠀⣠⠖⠋⠒⠀⠀⠀⠀⢀⣀⡀⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⡇⠀⠀⡏⠀⢰⣷⡆⠀⠀⠀⠸⣿⣿⠀⣳⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠓⣒⡲⣦⣥⣤⣀⡃⣀⣸⣿⡧⠤⠴⡶⠖⣿⠛⢛⣿⠁⠀⣸⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠈⢹⡅⠈⢉⣿⣧⣤⠟⣬⢿⠒⠚⣫⡋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⡀⢠⡀⠀⠀⠀⠀⠀⠉⠉⠻⡿⠀⠀⠀⡟⠧⠆⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠑⠒⢲⠢⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠀⠀⢸⣿⠀⠀⠀⠀⠀⢀⡀⣀⠀⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⣿⣿⣤⣤⣤⣧⣽⣼⡷⠛⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠑⢄⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣀⠈⠛⠿⢿⣿⡿⡿⠿⠃⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠄⠀⠂⢤⠮⣄⡀⠀⠉⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠉⠒⠲⠤⠤⠤⠤⠤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠭⢒⣲⡬⠤⠤⢼⡆⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⢴⡦⠊⢻⣍⠒⠤⠤⠲⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣀⠀⠀⠉⠉⠉⡍⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠚⠉⠁⢠⣊⡀⠀⢀⢫⠑⠒⠒⠂⠉⡠⠊⠑⡆⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢊⣩⢾⠈⠉⠐⠒⠒⢺⠁⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠈⢩⠋⠀⣇⠀⠀⣠⠎⣇⡀⠀⠘⡀⠀⠑⠤⡀⠀⠀⠀⠀⠀⠀⡏⣎⣕⠒⣾⢷⢉⡽⠤⢤⠇⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⡀⠀⠘⣄⠔⠁⠀⢰⠀⠈⠉⠉⠀⠀⠀⠙⡄⠀⠀⠀⠀⢸⢚⢌⡲⠀⢿⡙⠀⠤⢄⡜⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⣀⢻⣀⠠⠔⠚⠁⠀⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠸⢸⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⢐⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⢸⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠊⠀⠀⢸⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠲⡉⠢⡀⠀⢀⠠⠂⢨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠈⠱⢴⠒⠢⡈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⣀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
]

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
	for index, item in enumerate(menu_item.key()):
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

##그리기함수:세로로 메뉴를 나열(딕셔너리 사용)(키값에따라 하단부에 설명 추가)
def menu_vertical_dic(selected_window, dic_menu ,menu_item, selected_row, middle_hight, middle_width, max_hight, max_width, max_width_left):
	for index, (key, item) in enumerate(dic_menu.items[menu_item]):
		key_x = middle_width - len(key)//2
		key_y = middle_hight - len(dic_item) + index * 2 - 7

		if index == selected_row:
			selected_window.addstr(key_y, key_x, item, SELECT_COLOR)

			item_x = middle_width - len(item)//2
			item_y = max_hight - 9 
			selected_window.addstr(max_width_left + 2, item_y - 2, )
			for i in range(max_width_left + 2, max_width - 2):
				selected_window.addstr(item_y -2 , i,"─")
			selected_window.addstr(item_y, item_x, item)
		else:
			selected_window.addstr(key_y, key_x, item)

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
	bot_screen_hight , bot_screen_width = max_hight-2, max_width
	left_screen_hight, left_screen_width = max_hight-3, 20
	right_screen_hight, right_screen_width = max_hight-3, max_width 
	
	##맨 위 화면은 [사용자						날짜] 형식으로 표시
	stdscr.clear()
	stdscr.addstr(top_screen_hight, 0, DATE.rjust(top_screen_width," "), MAIN_COLOR_REVERSE)
	stdscr.addstr(top_screen_hight, 0, USER,MAIN_COLOR_REVERSE)
	
	##맨 밑 화면 첫번째 줄은 D-PAD를 이용하라는 문구, 두번째 줄은 특수 버튼 지정(현재는 가장 우측것만 종료)
	stdscr.addstr(bot_screen_hight, 0, "Use D-PAD and A button to select menu".center(bot_screen_width-1, ' '), MAIN_COLOR_REVERSE)
	stdscr.addstr(bot_screen_hight+1, 0, "SHUT DOWN  ".rjust(bot_screen_width-1, ' '))
	
	##중앙 좌측화면과 우측화면을 나누는 선 그리기
	for i in range(top_screen_hight+3, bot_screen_hight-3):
		stdscr.addstr(i, left_screen_width,"│")

	##화면 중앙 좌측은 메인메뉴 표시
	selected_left_menu = 0
	menu_vertical_1(stdscr, Main_menu, selected_left_menu, left_screen_hight//2, left_screen_width//2 )

	##화면 우측은 세부메뉴에 따라서 다르게 표시 
	drew_ASCIIart(stdscr, juice, (right_screen_hight-top_screen_hight)//2 +top_screen_hight, (right_screen_width -left_screen_width)//2 +left_screen_width)

	stdscr.refresh()

	##메인 메뉴 선택 작동
	while True:
		key = stdscr.getch()
		if key == curses.KEY_UP and selected_left_menu > 0:
			selected_left_menu -= 1
		elif key == curses.KEY_DOWN and selected_left_menu < len(Main_menu)-1 :
			selected_left_menu += 1
		elif key == curses.KEY_ENTER or key in [10, 13]:
			selected_main_menu = list(Main_menu.keys())[selected_left_menu]
			break

		menu_vertical_1(stdscr, Main_menu, selected_left_menu, left_screen_hight//2, left_screen_width//2 )
		stdscr.refresh()

	
	##선택한 메인 메뉴에 맞추어서 화면 변경

	##이전 화면 다 지우고 상단,하단화면 다시 표시
	##맨 위 화면은 [사용자						날짜] 형식으로 표시
	stdscr.clear()
	stdscr.addstr(top_screen_hight, 0, DATE.rjust(top_screen_width," "), MAIN_COLOR_REVERSE)
	stdscr.addstr(top_screen_hight, 0, USER,MAIN_COLOR_REVERSE)
	
	##맨 밑 화면 첫번째 줄은 D-PAD를 이용하라는 문구, 두번째 줄은 특수 버튼 지정(현재는 가장 우측것만 종료)
	stdscr.addstr(bot_screen_hight, 0, "Use D-PAD and A button to select menu".center(bot_screen_width-1, ' '), MAIN_COLOR_REVERSE)
	stdscr.addstr(bot_screen_hight+1, 0, "SHUT DOWN  ".rjust(bot_screen_width-1, ' '))
	
	##중앙 좌측화면과 우측화면을 나누는 선 그리기
	for i in range(top_screen_hight+3, bot_screen_hight-3):
		stdscr.addstr(i, left_screen_width,"│")
	

	##좌측 상단에 선택한 메뉴 하이라이트 표시
	stdscr.addstr(top_screen_hight+4, (left_screen_width - len(selected_main_menu))//2, selected_main_menu, curses.A_BOLD )

	##좌측 화면에 세부 메뉴 표시
	selected_left_menu = 0
	menu_vertical_1(stdscr, Main_menu[selected_main_menu], selected_left_menu, left_screen_hight//2 +1, left_screen_width//2 )
	stdscr.refresh()

	##우측 화면에 선택된 세부메뉴 설명 표시
	stdscr.addstr((right_screen_hight -top_screen_hight)//2 +top_screen_hight, (right_screen_width -left_screen_width)//2 +left_screen_width -len(list(Main_menu[selected_main_menu].values())[0])//2, list(Main_menu[selected_main_menu].values())[0])
	stdscr.refresh()

	##좌측 메뉴 선택 작동 및 우측 설명칸 작동
	while True:
		key = stdscr.getch()
		if key == curses.KEY_UP and selected_left_menu > 0:
			selected_left_menu -= 1
		elif key == curses.KEY_DOWN and selected_left_menu < len(Main_menu[selected_main_menu])-1 :
			selected_left_menu += 1
		elif key == curses.KEY_ENTER or key in [10, 13]:
			##선택한 세부 메뉴에 따른 프로그램 실행
			selected_sub_menu = Main_menu[selected_main_menu][selected_left_menu]
			os.system(f"python {selected_sub_menu}.py")
			sys.exit()
					
		menu_vertical_1(stdscr, Main_menu[selected_main_menu], selected_left_menu, left_screen_hight//2 +1, left_screen_width//2 )
		for i in range(left_screen_width+1,right_screen_width):
			stdscr.addstr((right_screen_hight -top_screen_hight)//2 +top_screen_hight,i," ")
		stdscr.addstr((right_screen_hight -top_screen_hight)//2 +top_screen_hight, (right_screen_width -left_screen_width)//2 +left_screen_width -len(list(Main_menu[selected_main_menu].values())[selected_left_menu])//2, list(Main_menu[selected_main_menu].values())[selected_left_menu])
		stdscr.refresh()
		
	

curses.wrapper(main)
##│┐┌ ─ ┘└
	