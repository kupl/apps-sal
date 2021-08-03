from collections import deque
from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    s = list(input())
    n = len(s)
    ans = [0] * n
    x = 0
    y = 0
    a = n - 1
    b = n - 1
    stack = deque([])
    prev = -1
    while a >= 0:
        if s[a] == ')':
            stack.append(a)
            ans[a] = prev
        else:
            if len(stack) == 0:
                ans[a] = -1
                prev = -1
            else:
                prev = stack[-1] + 1
                ans[a] = prev
                stack.pop()
        a -= 1

    q = int(input())
    x = list(map(int, input().split()))
    for i in x:
        i = i - 1
        print(ans[i])
