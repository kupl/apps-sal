from sys import stdin
n, m = list(map(int, stdin.readline().strip().split()))
s = list(map(int, stdin.readline().strip().split()))
high = m + 1
low = 0
while (high - low) > 1:
    mx = 0
    flag = True
    mid = (low + high) // 2

    for i in range(n):
        if (s[i] >= mx):
            if(s[i] + mid) >= m and (s[i] + mid) % m >= mx:
                continue
            else:
                mx = s[i]
        elif (s[i] + mid) >= mx:
            continue
        else:
            flag = False
            break
    if flag:
        high = mid
    else:
        low = mid
for j in range(low, low + 2):
    mx = 0
    flag = True
    mid = (j + j + 1) // 2
    for i in range(n):
        if (s[i] >= mx):
            if(s[i] + mid) >= m and (s[i] + mid) % m >= mx:
                continue
            else:
                mx = s[i]
        elif (s[i] + mid) >= mx:
            continue
        else:
            flag = False
            break
    if flag:
        print(j)
        break
