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
    TOP_WINDOW=curses.newwin(1,coulmns,0,0)
    RIGHT_WINDOW=curses.newwin(row-3,coulmns//2-1,1,coulmns//2)
    LEFT_WINDOW=curses.newwin(row-3,coulmns//2-2,1,1)
    BOTTOM_WINDOW=curses.newwin(2,coulmns,row-2,0)

##첫화면:기본 설정 확인
    ##첫화면:미리 설정된 기본 설정 확인
    USER = getpass.getuser()
    DATE = str(time.strftime('%Y-%m-%d'))
    RAW_INFO = os.uname()
    ARC_INFO = RAW_INFO[4]
    OS_INFO = RAW_INFO[3].split(" ")   

    INFO_FILE = open('info.txt')
    VERS,UPDATE = INFO_FILE.read().split("\n")
    INFO_FILE.close()

    ##첫화면:미리 설정된 기본 설정 표시
    RIGHT_WINDOW.clear()
    RIGHT_WINDOW.addstr(row//2-4,1,f" USER:{USER}")
    RIGHT_WINDOW.addstr(row//2-2,1,f" {VERS}")
    RIGHT_WINDOW.addstr(row//2,1,f" {UPDATE}")
    RIGHT_WINDOW.addstr(row//2+2,8,f"{OS_INFO[0]}")
    RIGHT_WINDOW.addstr(row//2+2,1,f" {ARC_INFO}")
    RIGHT_WINDOW.refresh()

    ##첫화면:로고표시
    LEFT_WINDOW.clear()
    LEFT_WINDOW.addstr(row//2-6,coulmns//2-25,"⠀⠀⠀⠀⠀⠀⢀⡠⠔⠊⡟⠲⢤⣀⠀⠀⠀⠀⠀⠀⠀")
    LEFT_WINDOW.addstr(row//2-5,coulmns//2-25,"⠀⠀⢀⣠⣄⣀⢸⠀⠀⠀⡇⠀⠀⢸⠀⣀⣄⣀⠀⠀⠀")
    LEFT_WINDOW.addstr(row//2-4,coulmns//2-25,"⡴⠚⠁⢸⣿⣿⣿⠀⠀⠀⡇⠀⠀⢸⡿⠋⠀⠈⠙⣢⠄")
    LEFT_WINDOW.addstr(row//2-3,coulmns//2-25,"⡇⠀⠀⢸⡿⠟⠋⠀⠀⠀⡇⠀⠀⠈⠀⠀⠀⢀⡼⠁⠀")
    LEFT_WINDOW.addstr(row//2-2,coulmns//2-25,"⡇⠀⠀⠈⠀⠀⣀⠀⠀⠀⡇⠀⠀⢰⠀⠀⠠⡎⠀⠀⠀")
    LEFT_WINDOW.addstr(row//2-1,coulmns//2-25,"⡇⠀⠀⢠⣶⣿⣿⠀⠀⠀⡇⠀⠀⢸⣧⠀⠀⢳⡀⠀⠀")
    LEFT_WINDOW.addstr(row//2-0,coulmns//2-25,"⡇⠀⠀⢸⣿⣿⣿⣀⠤⠖⠓⠦⣀⣸⣿⣆⠀⠀⢳⠀⠀")
    LEFT_WINDOW.addstr(row//2+1,coulmns//2-25,"⡇⠀⠀⢸⣿⣿⣿⣤⣀⠀⠀⢀⣤⣿⣿⣿⣆⠀⠀⢧⠀")
    LEFT_WINDOW.addstr(row//2+2,coulmns//2-25,"⡧⠔⠋⠁⠈⠛⠻⣿⠀⠉⠋⠀⢻⣿⠿⠋⠁⠉⠓⠬⣇")
    LEFT_WINDOW.addstr(row//2+3,coulmns//2-25,"⠉⠐⠦⣀⡠⠔⠊⠁⠀⠀⠀⠀⠀⠉⠒⠦⣄⡠⠔⠊⠉")    
    LEFT_WINDOW.refresh()

    ##첫화면:상단바 표시
    TOP_WINDOW.clear()
    TOP_WINDOW.addstr(0,0,f"{USER}".ljust(coulmns-1),MAIN_COLOR_REVERSE)
    TOP_WINDOW.addstr(0,coulmns-len(str(DATE))-1,f"{DATE}",MAIN_COLOR_REVERSE)
    TOP_WINDOW.refresh()

    ##첫화면:하단바 표시
    BOTTOM_WINDOW.clear()
    BOTTOM_WINDOW.addstr(0,0,"CHECK SETTING".center(coulmns-1))
    BOTTOM_WINDOW.addstr(1,0,"CHANGE          NEXT   BACK".center(coulmns-1),MAIN_COLOR_REVERSE)
    BOTTOM_WINDOW.refresh()

    ##첫화면:입력에 따른 화면 전환
    while True:   
        MOD=int(BOTTOM_WINDOW.getch())-48    
        if MOD==5:
            break
        elif MOD==1:
            stdscr.clear()
            os.system("python3.6 CHG_SET.py")
        elif MOD==6:
            stdscr.clear()
            os.system("python3.6 BOOT_MENU.py")
            exit

##두번쨰화면:현재 기기 검사 -- 모듈 및 실 기기 제작 후 추가 예정
    ##두번째화면:장착된 모듈 인식

    ##두번째화면:모듈 정보 표시

    ##두번쨰화면:모듈 로고 표시

    ##두번쨰화면:하단바 표시
    BOTTOM_WINDOW.clear()
    BOTTOM_WINDOW.addstr(0,0,"ADDON SETTING".center(coulmns-1))
    BOTTOM_WINDOW.addstr(1,0,"CHANGE       GO TO MAIN  BACK".center(coulmns-1),MAIN_COLOR_REVERSE)
    BOTTOM_WINDOW.refresh()

    ##두번째화면:입력에 따른 화면 전환
    while True:   
        MOD=int(BOTTOM_WINDOW.getch())-48    
        if MOD==5:
            stdscr.clear()
            os.system("python3.6 MAIN_MENU.py")
            break
        elif MOD==1:
            stdscr.clear()
            os.system("python3.6 CHG_ADD.py")
            break
        elif MOD==6:
            stdscr.clear()
            os.system("python3.6 SYS_STR.py")
            break


    LEFT_WINDOW.clear()
    RIGHT_WINDOW.clear()
    LEFT_WINDOW.refresh()
    RIGHT_WINDOW.refresh()



wrapper(main)