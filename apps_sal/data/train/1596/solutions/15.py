"""
Name : Vasu Gamdha
codechef id :vasu_vg
Problem : CRCLJUMP

##############################
### LOGIC STAYS BETWEEN US ###
##############################
"""
from sys import stdin as sin, stdout as sout
MOD = 1000000007
for _ in range(int(sin.readline())):
    (x, y) = map(int, sin.readline().split())
    (x, y) = (x + 1, y + 1)
    (xx, yy) = (bin(x).count('1'), bin(y).count('1'))
    ans = str(xx) + ' ' + str(yy)
    if xx == yy:
        sout.write(str('0 0') + '\n')
    elif xx > yy:
        sout.write(str('2 ') + str(xx - yy) + '\n')
    else:
        sout.write(str('1 ') + str(yy - xx) + '\n')
