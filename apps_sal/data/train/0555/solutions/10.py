import sys
for __ in range(eval(input())):
    n = eval(input())
    lists = list(map(int, sys.stdin.readline().split()))
    (curmax, temp, fflag) = (0, 2, False)
    for i in range(2, n):
        if lists[i - 2] + lists[i - 1] == lists[i]:
            temp += 1
        else:
            if temp > curmax:
                curmax = temp
            temp = 2
    print(max(curmax, temp) if n > 1 else 1)
