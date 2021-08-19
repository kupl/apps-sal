import math
t = int(input())
for test in range(t):
    (n, m) = list(map(int, input().split()))
    up = 0
    down = 0
    left = 0
    right = 0
    s = input()
    f = 0
    for i in s:
        if i == 'L':
            left += 1
            if right > 0:
                right -= 1
            if left == m:
                break
        if i == 'R':
            right += 1
            if left > 0:
                left -= 1
            if right == m:
                break
        if i == 'U':
            up += 1
            if down > 0:
                down -= 1
            if up == n:
                break
        if i == 'D':
            down += 1
            if up > 0:
                up -= 1
            if down == n:
                break
    if abs(down) < n and abs(up) < n and (abs(left) < m) and (abs(right) < m):
        print('safe')
    else:
        print('unsafe')
