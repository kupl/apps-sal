import sys
import math
from collections import defaultdict, Counter
input = sys.stdin.readline


def print(x):
    sys.stdout.write(str(x) + '\n')


t = int(input())
for i in range(t):
    s = input().strip()
    c = 0
    v = [0] * len(s)
    st = []
    prev = -2
    c1 = 0
    for j in range(len(s) - 1, -1, -1):
        if s[j] == ')':
            v[j] = prev
            st.append(j)
        else:
            c1 += 1
            c += 1
            if st:
                v[j] = st.pop()
            else:
                v[j] = -2
            prev = v[j]
    q1 = int(input())
    q = list(map(int, input().split()))
    for j in q:
        print(v[j - 1] + 1)
