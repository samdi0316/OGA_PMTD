# -*- coding:utf-8 -*-

import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import os
import os.path
import time
import getpass

def main(stdscr):
##설정준비:미리 자주사용할 함수나 색상들을 설정
    ##설정준비:색상
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)     
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)  
       
    MAIN_COLOR=curses.color_pair(1)
    MAIN_COLOR_REVERSE=curses.color_pair(2)

    ##설정준비:터미널 사이즈 조사
    R_row,R_coulumn=os.popen('stty size', 'r').read().split()
    row=int(R_row)
    coulmns=int(R_coulumn)

    ##설정준비:파일 검색 함수
    def findfile(name, path):
        for dirpath, dirname, finding_name in os.walk(path):
            if name in finding_name:
                return os.path.join(dirpath, name)

##첫화면:기본 설정 확인 및 운용전 검사
    ##첫화면:화면분할 
    TOP_WINDOW=curses.newwin(1,coulmns,0,0)
    RIGHT_WINDOW=curses.newwin(row-3,coulmns//2-1,1,coulmns//2)
    LEFT_WINDOW=curses.newwin(row-3,coulmns//2-2,1,1)
    BOTTOM_WINDOW=curses.newwin(2,coulmns,row-2,0)

    ##첫화면:하단바 표시
    BOTTOM_WINDOW.clear()
    BOTTOM_WINDOW.addstr(0,0,"CHECK SETTING".center(coulmns-1))
    BOTTOM_WINDOW.addstr(1,0," ".center(coulmns-1),MAIN_COLOR_REVERSE)
    BOTTOM_WINDOW.refresh()

    ##첫화면:미리 설정된 기본 설정 확인
    USER = getpass.getuser()
    DATE = str(time.strftime('%Y-%m-%d'))
    
    open("info.txt",'r')
    VERS = 
    
    ##첫화면:미리 설정된 기본 설정 표시
    TOP_WINDOW.clear()
    TOP_WINDOW.addstr(0,0,f"{USER}".ljust(coulmns-1),MAIN_COLOR_REVERSE)
    TOP_WINDOW.addstr(0,coulmns-len(str(DATE))-1,f"{DATE}",MAIN_COLOR_REVERSE)
    TOP_WINDOW.refresh()

    ##







    BOTTOM_WINDOW.getch()

wrapper(main)