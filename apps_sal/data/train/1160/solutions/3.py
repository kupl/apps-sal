from random import *


def check(h):
    ans = True
    for i in range(n - 1):
        if i % 2 == 0:
            if h[i] < h[i + 1]:
                ans = True
            else:
                ans = False
                break
        elif h[i] > h[i + 1]:
            ans = True
        else:
            ans = False
            break
    if ans == True:
        return 1
    ans = True
    for i in range(n - 1):
        if i % 2 == 1:
            if h[i] < h[i + 1]:
                ans = True
            else:
                ans = False
                break
        elif h[i] > h[i + 1]:
            ans = True
        else:
            ans = False
            break
    if ans == True:
        return 1
    return 0


for t in range(int(input())):
    n = int(input())
    h = []
    r = []
    for i in range(n):
        (x, y) = list(map(int, input().split()))
        h.append(x)
        r.append(y)
    ans = []
    curr = check(h)
    if curr != 0:
        ans.append(0)
    for i in range(1, 20):
        for j in range(n):
            h[j] += r[j]
        temp = check(h)
        if temp != curr:
            if temp == 0:
                ans.append(i - 1)
            elif temp == 1 and curr == 0:
                ans.append(i)
            elif temp == 2 and curr == 0:
                ans.append(i)
            elif temp == 1 and curr == 2:
                ans.append(i - 1)
                ans.append(i)
            elif temp == 2 and curr == 1:
                ans.append(i - 1)
                ans.append(i)
        curr = temp
        if len(ans) == 3:
            break
    if len(ans) % 2 == 1:
        ans.append('Inf')
    print(len(ans) / 2)
    for i in range(0, len(ans), 2):
        print(ans[i], ans[i + 1])
