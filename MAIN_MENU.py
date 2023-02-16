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

    ##설정준비:화면분할 
    TOP_WINDOW=curses.newwin(2,coulmns,0,0)
    RIGHT_WINDOW=curses.newwin(row-4,coulmns//2+16,2,15)
    LEFT_WINDOW=curses.newwin(row-4,15,2,1)
    BOTTOM_WINDOW=curses.newwin(2,coulmns,row-2,0)

##메뉴설정:세부 메뉴들을 딕셔너리 형태로 미리 설정
    ##통신메뉴:와이파이,I2C,시리얼 통신을 설정,송수신 표시
    ##통신메뉴:와이파이
    
    ##통신메뉴:I2C

    ##통신메뉴:시리얼 통신

    ##GPIO메뉴:GPIO를 제어,입력값을 표시
    ##GPIO메뉴:GPIO 제어 프로그램


    ##설정메뉴

##초기화면:설정한 메뉴들중에서 선택, 실행
    ##초기화면:현재 커서가 있는 위치를 저장
    COSOR = 0
    COS_DIR = "/MAIN_MENU"

    RIGHT_WINDOW.clear()
    RIGHT_WINDOW.addstr(row//2-2,coulmns//2-21,"use arrow key")
    RIGHT_WINDOW.addstr(row//2-1,coulmns//2-21,"to select menu")
    RIGHT_WINDOW.refresh()

    ##초기화면:좌측 초기 매뉴 표시
    LEFT_WINDOW.clear()
    LEFT_WINDOW.addstr(1,0,"MAIN MENU".center(15),MAIN_COLOR_REVERSE)
    LEFT_WINDOW.addstr(2,0,'commuication'.center(15))
    LEFT_WINDOW.addstr(3,0,'GPIO'.center(15))
    LEFT_WINDOW.addstr(4,0,'setting'.center(15))
    LEFT_WINDOW.refresh()

    ##첫화면:상단바 표시
    TOP_WINDOW.clear()
    TOP_WINDOW.addstr(0,0,"hi".ljust(coulmns-1),MAIN_COLOR_REVERSE)
    TOP_WINDOW.addstr(0,coulmns-5,"DATE",MAIN_COLOR_REVERSE)
    TOP_WINDOW.addstr(1,0,f"{COS_DIR}".ljust(coulmns-1),MAIN_COLOR_REVERSE)
    TOP_WINDOW.refresh()

    ##첫화면:하단바 표시
    BOTTOM_WINDOW.clear()
    BOTTOM_WINDOW.addstr(0,0,"SELET MENU".center(coulmns-1))
    BOTTOM_WINDOW.addstr(1,0,"Ⅰ    Ⅱ   Ⅲ   Ⅳ   Ⅳ   Ⅵ".center(coulmns-1),MAIN_COLOR_REVERSE)
    BOTTOM_WINDOW.refresh()

    LEFT_WINDOW.getch()



wrapper(main)