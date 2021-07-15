import sys
import datetime
a,b,c = list(map(int,sys.stdin.readline().split()))
d = datetime.date(c,b,a)
print(d.strftime("%A"))
