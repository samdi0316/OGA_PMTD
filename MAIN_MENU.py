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
    curses.init_pair(3,curses.COLOR_MAGENTA,curses.COLOR_WHITE)
       
    MAIN_COLOR = curses.color_pair(1)
    MAIN_COLOR_REVERSE = curses.color_pair(2)
    SELECT_COLOR = curses.color_pair(3)

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
    LEFT_WINDOW.addstr(1,2,"MAIN MENU".center(13),MAIN_COLOR_REVERSE)
    LEFT_WINDOW.addstr(2,2,'commuication'.center(13))
    LEFT_WINDOW.addstr(3,2,'GPIO'.center(13))
    LEFT_WINDOW.addstr(4,2,'setting'.center(13))
    LEFT_WINDOW.refresh()

    #초기화면:상단바 표시
    TOP_WINDOW.clear()
    TOP_WINDOW.addstr(0,0,"hi".ljust(coulmns-1),MAIN_COLOR_REVERSE)
    TOP_WINDOW.addstr(0,coulmns-5,"DATE",MAIN_COLOR_REVERSE)
    TOP_WINDOW.addstr(1,0,f"{COS_DIR}".ljust(coulmns-1),MAIN_COLOR_REVERSE)
    TOP_WINDOW.refresh()

    ##초기화면:하단바 표시
    BOTTOM_WINDOW.clear()
    BOTTOM_WINDOW.addstr(0,0,"SELECT MENU".center(coulmns-1))
    BOTTOM_WINDOW.addstr(1,0,"Ⅰ    Ⅱ   Ⅲ   Ⅳ   Ⅳ   Ⅵ".center(coulmns-1),MAIN_COLOR_REVERSE)
    BOTTOM_WINDOW.refresh()

##커서조작:D-PAD의 입력에 따라 커서가 이동,화면이 전환됨   
    ##커서조작:현재 커서가 있는 위치를 저장
    COSOR = 0
    COS_DIR = "/MAIN_MENU"    
    
    ##커서조작:

    LEFT_WINDOW.getch()



wrapper(main)