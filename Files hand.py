import os
import random as r
try:
    print("resource opened")
    print()
    f=open("C:\\Users\\gokul\\OneDrive\\Documents\\a1.txt",'r+')
    if os.path.exists("C:\\Users\\gokul\\OneDrive\\Documents\\a1.txt"):
        print("the file exist")
        print()
        for i in f:
            print(i,end='')
    f.close()
except OSError:
    print("The file does no exist")
finally:
    print()
    print()
    print("resource closed")