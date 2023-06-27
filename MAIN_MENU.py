# -*- coding:utf-8 -*-

import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import os
import os.path
import time
import getpass

##함수준비:자주 사용하는 함수들을 미리 정의
##함수준비:세로로 메뉴를 만드는 함수
def print_vertical_menu(stdscr, menu, selected_row_idx):
    
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

##함수준비:가로로 메뉴를 만드는 함수
def print_horizontal_menu(stdscr, menu , selected_cul_idx):
    al = 0
    ex = 0
    h, w = stdscr.getmaxyx()

    for cul in menu:
    	al = al + len(cul)
    
    for idx, row in enumerate(menu):
    	for cul in menu:
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

##함수준비:정중앙에 원하는 문자를 출력하는 함수
def print_center(stdscr, text):
    
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

##함수준비:파일 검색 함수
def findfile(name, path):
    for dirpath, dirname, finding_name in os.walk(path):
        if name in finding_name:
            return os.path.join(dirpath, name)
    
    
def main(stdscr):
##설정준비:미리 자주사용할 자료나 색상들을 설정
    ##설정준비:색상
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)     
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)
    curses.init_pair(3,curses.COLOR_MAGENTA,curses.COLOR_WHITE)
       
    MAIN_COLOR = curses.color_pair(1)
    MAIN_COLOR_REVERSE = curses.color_pair(2)
    SELECT_COLOR = curses.color_pair(3)

    ##설정준비:터미널 사이즈 조사
    R_row,R_coulumn=os.popen('stty size', 'r').read().split()
    row=int(R_row)
    coulmns=int(R_coulumn)

    ##설정준비:화면분할 
    TOP_WINDOW=curses.newwin(2,coulmns,0,0)
    RIGHT_WINDOW=curses.newwin(row-4,coulmns//2+25,2,18)
    LEFT_WINDOW=curses.newwin(row-4,17,2,1)
    BOTTOM_WINDOW=curses.newwin(2,coulmns,row-2,0)

##메뉴설정:세부 메뉴들을 딕셔너리 형태로 미리 설정
    ##통신메뉴:와이파이,I2C,시리얼 통신을 설정,송수신 표시
    ##통신메뉴:와이파이
    
    ##통신메뉴:I2C

    ##통신메뉴:시리얼 통신

    ##GPIO메뉴:GPIO를 제어,입력값을 표시
    ##GPIO메뉴:GPIO 제어 프로그램


    ##설정메뉴

##초기화면:메뉴들을 표시
    ##초기화면:우측 메뉴 세부내용 창
    RIGHT_WINDOW.clear()
    rectangle(RIGHT_WINDOW,0,1,row-5,coulmns//2+23)
    RIGHT_WINDOW.addstr(row//2-2,2,"use D-PAD".center(coulmns//2+21))
    RIGHT_WINDOW.addstr(row//2-1,2,"to select menu".center(coulmns//2+21))
    RIGHT_WINDOW.refresh()

    ##초기화면:좌측 초기 매뉴 
    LEFT_WINDOW.clear()
    rectangle(LEFT_WINDOW,0,0,row-5,15)
    LEFT_WINDOW.refresh()

    #초기화면:상단바 표시
    TOP_WINDOW.clear()
    TOP_WINDOW.addstr(0,0,"hi".ljust(coulmns-1),MAIN_COLOR_REVERSE)
    TOP_WINDOW.addstr(0,coulmns-5,"DATE",MAIN_COLOR_REVERSE)
##    TOP_WINDOW.addstr(1,0,f"{MENU_idx}".ljust(coulmns-1),MAIN_COLOR_REVERSE)
    TOP_WINDOW.refresh()

    ##초기화면:하단바 표시
    BOTTOM_WINDOW.clear()
    BOTTOM_WINDOW.addstr(0,0,"SELECT MENU".center(coulmns-1))
    BOTTOM_WINDOW.addstr(1,0,"Ⅰ    Ⅱ   Ⅲ   Ⅳ   Ⅳ   Ⅵ".center(coulmns-1),MAIN_COLOR_REVERSE)
    BOTTOM_WINDOW.refresh()

##커서조작:D-PAD의 입력에 따라 커서가 이동,화면이 전환됨   
    ##커서조작:현재 커서가 있는 위치 및 메뉴 내용을 자료로 저장
    COSOR = 0
    MENU_idx= "Main Menu" 
    MAIN_MENU = ['commuication', 'GPIO' , 'Setting']
        
    ##커서조작:
    print_vertical_menu(LEFT_WINDOW, MAIN_MENU, COSOR)

    while 1:
    	key = LEFT_WINDOW.getch()

    	if key == curses.KEY_UP and COSOR > 0:
    		COSOR -= 1
    	elif key == curses.KEY_DOWN and COSOR < len(MAIN_MENU)-1:
    		COSOR += 1
    	elif key == curses.KEY_ENTER or key in [10, 13]:
    		LEFT_WINDOW.clear()
    		print_center(LEFT_WINDOW, f"You selected '{format(MAIN_MENU[COSOR])}'")
    		LEFT_WINDOW.getch()
    	
    	LEFT_WINDOW.clear()
    	print_vertical_menu(LEFT_WINDOW, MAIN_MENU, COSOR)
    	rectangle(LEFT_WINDOW,0,0,row-5,15)

    LEFT_WINDOW.getch()



wrapper(main)