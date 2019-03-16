__author__ = 'student'
import datetime, sys
jakasData = sys.argv[1]
cos = jakasData.split("-")
d0 = datetime.date(int(cos[0]), int(cos[1]), int(cos[2]))
d1 = datetime.datetime.now()
d2 = datetime.date(d1.year, d1.month, d1.day)
delta = d2 - d0
print(delta.days)

