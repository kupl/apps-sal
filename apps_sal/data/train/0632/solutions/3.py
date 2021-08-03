import sys
import math
t = int(sys.stdin.readline())
while t:

    s = (sys.stdin.readline())
    if(len(s) == 0):
        break
    s1 = s.split(' ')
    n = int(s1[0])
    k = int(s1[1])
    if ((k + 1) % int(math.pow(2, n)) == 0):
        print("ON")
    else:
        print("OFF")
    t -= 1
