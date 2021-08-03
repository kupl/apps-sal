from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())

    a = input().strip()
    b = input().strip()

    Q = deque(a)

    L = []
    while Q:
        L.append(Q.popleft())

        if Q:
            L.append(Q.pop())

    ANS = []
    for i in range(n):
        if i % 2 == 0:
            if L[i] == b[-1 - i]:
                ANS.append(1)
        else:
            if L[i] != b[-1 - i]:
                ANS.append(1)

        ANS.append(n - i)

    print(len(ANS), *ANS)
