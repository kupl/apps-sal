import bisect
l = [1, 5, 9, 15, 21]
for i in range(int(input())):
    s = input()
    sum = 0
    for k in s:
        x = ord(k) - ord('a') + 1
        y = bisect.bisect(l, x)
        if y == 0:
            sum += l[0] - x
        elif y == 5:
            sum += x - l[4]
        else:
            sum += min(x - l[y - 1], l[y] - x)
    print(sum)
