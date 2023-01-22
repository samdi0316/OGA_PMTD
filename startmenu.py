import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import os
import os.path
import time

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

    ##첫화면:실행 모드 선택
    ##첫화면:화면분할
    RIGHT_WINDOW=curses.newwin(row-2,coulmns//2-1,1,coulmns//2)
    LEFT_WINDOW=curses.newwin(row-2,coulmns//2-2,1,1)

    ##첫화면:실행모드 선택 메뉴
    RIGHT_WINDOW.clear()
    RIGHT_WINDOW.addstr(row//2-2,1,"Ⅰ : OPERATE SYS",MAIN_COLOR)
    RIGHT_WINDOW.addstr(row//2,1,"Ⅱ : SYS SETTING",MAIN_COLOR)
    RIGHT_WINDOW.addstr(row//2+2,1,"Ⅲ : SYS OFF",MAIN_COLOR)
    RIGHT_WINDOW.refresh()
    
    time.sleep(3)
    BUTTON_input=stdscr.getch()

    ##첫화면:버튼입력에 따라 실행모드 선택
##    MOD = int(0) 
##    while True:
##        
##        if BUTTON_input==1:
##            stdscr.clear()
##            MOD = int(1)
##            break
##        if BUTTON_input==2:
##            stdscr.clear()
##        if BUTTON_input==2:
##            stdscr.clear()
        

            

##    stdscr.clear()
##    stdscr.addstr(row-2,0,"Ⅰ    Ⅱ   Ⅲ   Ⅳ   Ⅳ   Ⅵ".center(coulmns),MAIN_COLOR_REVERSE)
##    stdscr.addstr(row-3,0,"SELET MODE".center(coulmns))
##    stdscr.refresh()
    
##    stdscr.getch()


wrapper(main)
