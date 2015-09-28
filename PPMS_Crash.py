'''
Created on 2015/3/17/

@author: QSong_pku
'''
import win32gui,time,os,ctypes,Skype4Py
from win32con import SW_SHOW
from ctypes import windll

ISOTIMEFORMAT='%Y-%m-%d %X'
while True:
    a=raw_input("Please input the name of the windows \n")
    win=win32gui.FindWindow(None,a)
    if win:
        break
    else:
        print time.strftime(ISOTIMEFORMAT,time.localtime(time.time())),'can not find the program,check the name of the window'
while True:
    win=win32gui.FindWindow(None,a)
    win32gui.ShowWindow(win,SW_SHOW)
    crash_or_not= windll.user32.IsHungAppWindow(win)
    if  crash_or_not:
        print time.strftime(ISOTIMEFORMAT,time.localtime(time.time())),'Program was crashed! Skype is calling......'
        skype=Skype4Py.Skype()
        skype.Attach()
        m_Phone='songqiskype'
        m_Phone2='zylicqm'
        m_Call=skype.PlaceCall(m_Phone)
        print 'calling',m_Phone,'.....'
        m_Call2=skype.PlaceCall(m_Phone2)
        print 'calling',m_Phone2,'...'
        break
    else:
        print time.strftime(ISOTIMEFORMAT,time.localtime(time.time())),"everything is ok...."
    time.sleep(60)
    