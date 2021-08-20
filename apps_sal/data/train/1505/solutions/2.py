n = int(input())
s = list(map(int, input().split()))
dans = 0
fd = 0
c = 0
count = 0
maxs = 0
fs = n
for i in range(n):
    if s[i] == 1:
        c -= 1
        count += 1
        if abs(c) > dans:
            dans = abs(c)
            if fd < i:
                fd = i
    else:
        c += 1
        if c == 0:
            if count > maxs:
                maxs = count + 1
                fs = i - maxs + 2
            count = 0
        else:
            count += 1
print(dans, fd + 1, maxs, fs)
