t = int(input())
for i in range(t):
    ax, ay, bx, by, cx, cy = map(int, input().split())
    x = min(ax, bx, cx)
    y = min(ay, by, cy)
    ans = 0
    if x >= 0 and y >= 0:
        if x == 0 and y == 0:
            pass
        else:
            ans += 1
    num = abs(abs(x) - abs(y))
    if x >= 0:
        if y >= 0:
            ans += max(num - 1, 0)
        else:
            if abs(x) > abs(y):
                ans += num
            else:
                ans += max(num - 1, 0)
    else:
        if y >= 0:
            if abs(y) > abs(x):
                ans += num
            else:
                ans += max(num - 1, 0)
        else:
            ans += max(num - 1, 0)
    ans += abs(x) + abs(y)
    if x >= 0:
        if y >= 0:
            if round((ax + bx + cx) / 3) == max(ax, bx, cx) and round((ay + by + cy) / 3) == max(ay, by, cy):
                ans += 1
            else:
                if abs(x) > abs(y):
                    if round((ax + bx + cx) / 3) == max(ax, bx, cx):
                        ans += 1
                elif abs(y) > abs(x):
                    if round((ay + by + cy) / 3) == max(ay, by, cy):
                        ans += 1
                elif x == 0 and y == 0:
                    if round((ax + bx + cx) / 3) == max(ax, bx, cx) or round((ay + by + cy) / 3) == max(ay, by, cy):
                        ans += 1
        else:
            if round((ax + bx + cx) / 3) == max(ax, bx, cx) and round((ay + by + cy) / 3) == min(ay, by, cy):
                ans += 1
            else:
                if abs(x) >= abs(y):
                    if round((ax + bx + cx) / 3) == max(ax, bx, cx):
                        ans += 1
                elif abs(y) > abs(x):
                    if round((ay + by + cy) / 3) == min(ay, by, cy):
                        ans += 1
    else:
        if y >= 0:
            if round((ax + bx + cx) / 3) == min(ax, bx, cx) and round((ay + by + cy) / 3) == max(ay, by, cy):
                ans += 1
            else:
                if abs(x) > abs(y):
                    if round((ax + bx + cx) / 3) == min(ax, bx, cx):
                        ans += 1
                elif abs(y) >= abs(x):
                    if round((ay + by + cy) / 3) == max(ay, by, cy):
                        ans += 1
        else:
            if round((ax + bx + cx) / 3) == min(ax, bx, cx) and round((ay + by + cy) / 3) == min(ay, by, cy):
                ans += 1
            else:
                if abs(x) > abs(y):
                    if round((ax + bx + cx) / 3) == min(ax, bx, cx):
                        ans += 1
                elif abs(y) > abs(x):
                    if round((ay + by + cy) / 3) == min(ay, by, cy):
                        ans += 1
    print(ans)
