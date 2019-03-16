__author__ = 'student'
import sys, math
delta = math.pow(float(sys.argv[2]),2) - 4 * (float(sys.argv[1])*float(sys.argv[3]))
if(delta>0):
    x_0=(-float(sys.argv[2])-math.sqrt((delta)))/(2*float(sys.argv[1]))
    x_1=(-int(sys.argv[2])+math.sqrt((delta)))/(2*float(sys.argv[1]))
    print(str(x_1) +" "+ str(x_0))
elif(delta==0):
    x_0=(-float(sys.argv[2]))/(2*float(sys.argv[1]))
    print(x_0)
else:
    print("0")