__author__ = 'student'
import sys

if sys.argv[2] == "+":
    print(int(sys.argv[1])+int(sys.argv[3]))
elif sys.argv[2] == "*":
    print(int(sys.argv[1])*int(sys.argv[3]))
elif sys.argv[2] == "-":
    print(int(sys.argv[1])-int(sys.argv[3]))
