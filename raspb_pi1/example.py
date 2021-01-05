#def str_operation(strn,num):
    #a = num * strn
    #print (a)
#str_operation(' Hello ',3)
import sys

def str_operation(strn,num):
    a = num * strn
    print (a)
str_operation(sys.argv[1],int(sys.argv[2]))