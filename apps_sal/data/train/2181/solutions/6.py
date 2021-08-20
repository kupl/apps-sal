(s, l, r) = (0, 0, int(input()) - 1)
t = list(map(int, input().split()))
while 1:
    while l < r and t[l] < t[l + 1]:
        l += 1
    while l < r and t[r] < t[r - 1]:
        r -= 1
    if l == r:
        break
    if t[l] < t[r]:
        s += t[l] - t[l + 1] + 1
        t[l + 1] = t[l] + 1
    else:
        s += t[r] - t[r - 1] + 1
        t[r - 1] = t[r] + 1
print(s)
