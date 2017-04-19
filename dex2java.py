#-*- coding:utf-8 -*-
#   
#   __Name__:       Dex2Java
#   __Author__:     tasfa
#   __Info__:       www.tasfa.cn
#   __Version__:    3.0


import subprocess
import sys

      
DEX2JAR_PATH='D:\\android-killer\\bin\dex2jar\\'                #config your dex2jar.bat's path here
JD_GUI_PATH='E:\jd-gui\jd-gui-windows-1.4.0\\'                  #config your jd-gui's path here
output=''                                                       #config your output jar's name here

def pathCheck():
    """
        Check the jar's path
    """
    global DEX2JAR_PATH
    global JD_GUI_PATH
    global output

    print " If you don't want to enter the path every time, you can set the path in the dex2Java.py !\n  "
    try:
        if not DEX2JAR_PATH:
            print "Please set your dex2jar.bat's path "
            path = raw_input()
            DEX2JAR_PATH = path
            print path
        if not JD_GUI_PATH:
            print "Please set your jd-gui's path "
            path = raw_input()
            JD_GUI_PATH=path
            print path
        if not output:
            print "Please set your output jar's path and name like d:\\output.jar!"
            jar = raw_input(">>>")
            output = jar
    except KeyboardInterrupt:
        print "user abort!"

def banner():
    """
        Print the banner and Version Info
    """
    print """ 
     _____          __       
    |_   _|_ _ ___ / _| __ _ 
      | |/ _` / __| |_ / _` |
      | | (_| \__ \  _| (_| |
      |_|\__,_|___/_|  \__,_|
                             
    """
    print "Welcome to use Dex2Java!"
    print "For more infomation --> www.tasfa.cn!!"
    print "<--------------------------------------------------->"



def dex2java():
    dexfile = sys.argv[1]

    #Force the parameters in order to reduce the user's input
    argv1_dex2jar='-f'
    argv2_dex2jar='-o'
    args = [DEX2JAR_PATH+'d2j-dex2jar.bat',dexfile,argv1_dex2jar,argv2_dex2jar,output]
    
    try:
        subprocess.call(args)
    except:
        pathCheck()

    args = [JD_GUI_PATH+'jd-gui.exe',output]
    try:
        subprocess.call(args)
    except:
        pathCheck()


def main():

    banner()
    try:
        pathCheck()
    except Exception:
        print "Path setup wrong!!!"
    dex2java()

if __name__ == '__main__':
    main()