# your code goes here
from sys import stdin, stdout
t = int(stdin.readline())
while t:
    t -= 1
    n = int(stdin.readline())
    maxi = -1
    index = 0
    for i in range(n):
        hh, mm, ss = list(map(int, stdin.readline().strip().split(':')))
        ssa = ss * 360.0 / 60.0
        mma = (mm + (ss / 60.0)) * 360.0 / 60.0
        hha = (hh + (mm + (ss / 60.0)) / 60.0) * 360.0 / 12.0
        avg = (abs(ssa - hha) + abs(mma - ssa) + abs(mma - hha)) / 3
        # print hha, mma, ssa
        if avg > maxi:
            maxi = avg
            index = i
    stdout.write(str(index + 1) + '\n')
