import sys
import math

for __ in range(eval(input())):
    n, m = list(map(int, sys.stdin.readline().split()))
    lists = list(map(int, sys.stdin.readline().split()))
    ans = []
    ans += lists[:m]
    ans += [math.ceil(x / 2) for x in lists[m:]]
    print("VICTORY" if sum(ans[:m]) >= sum(ans[m:]) else "DEFEAT")
