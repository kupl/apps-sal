import sys
import math
from collections import defaultdict, Counter
input = sys.stdin.readline


def print(x):
    sys.stdout.write(str(x) + '\n')


(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
avg1 = sum(a) // n
avg2 = avg1 + 1
m = a[n // 2]
ans1 = 0
ans2 = 0
ans3 = 0
if k == 1:
    for j in a:
        ans1 += abs(j - m)
        ans2 += abs(j - a[n // 2 - 1])
    if ans1 <= ans2:
        print(m)
    else:
        print(a[n // 2 - 1])
elif k == 2:
    for j in a:
        ans2 += abs(j - avg1) * abs(j - avg1)
        ans3 += abs(j - avg2) * abs(j - avg2)
    if ans2 <= ans3:
        print(avg1)
    else:
        print(avg2)
else:
    for j in a:
        ans2 += pow(abs(j - avg1), 3)
        ans3 += pow(abs(j - avg2), 3)
    if ans2 <= ans3:
        print(avg1)
    else:
        print(avg2)
