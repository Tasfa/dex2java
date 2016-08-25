#-*- coding:utf-8 -*-
#   
#   Name:       Dex2Java
#   Author:     tasfa
#   Info:       www.tasfa.cn
#   Version:    2.0


import subprocess
import sys

      
DEX2JAR_PATH=''                 #config your dex2jar.bat's path here
JD_GUI_PATH=''                  #config your jd-gui's path here
output=''                       #config your output jar's name here
def pathCheck():
    """
        Check the jar's path
    """
    global DEX2JAR_PATH
    global JD_GUI_PATH
    global output

    print "\33[32m If you don't want to enter the path every time, you can set the path in the dex2Java.py !\n \33[0m "
    try:
        if not DEX2JAR_PATH:
            print "Please set your dex2jar.bat's path "
            path = raw_input()
            DEX2JAR_PATH = path
        if not JD_GUI_PATH:
            print "Please set your jd-gui's path "
            path = raw_input()
            JD_GUI_PATH=path
        if not output:
            print "Please set your output jar's path and name like d:\\output.jar!"
            jar = raw_input()
            output = jar
    except KeyboardInterrupt:
        print "user abort!"

def banner():
    """
        Print the banner and Version Info
    """
    print """ \33[36m
     _____          __       
    |_   _|_ _ ___ / _| __ _ 
      | |/ _` / __| |_ / _` |
      | | (_| \__ \  _| (_| |
      |_|\__,_|___/_|  \__,_|
                             
    """
    print "Welcome to use Dex2Java!"
    print "For more infomation --> www.tasfa.cn!!"
    print "<--------------------------------------------------->\33[0m"


def main():

    banner()
    pathCheck()
    

    dexfile = sys.argv[1]

    #Force the parameters in order to reduce the user's input
    argv1_dex2jar='-f'
    argv2_dex2jar='-o'
    args = [DEX2JAR_PATH+'d2j-dex2jar.bat',dexfile,argv1_dex2jar,argv2_dex2jar,output]
    
    try:
        subprocess.call(args)
    except:
        pathcheck()

    args = [JD_GUI_PATH+'jd-gui.exe',output]
    try:
        subprocess.call(args)
    except:
        pathcheck()

if __name__ == '__main__':
    main()