m = int(input())
s = list(input())
d = [0 for _ in range(26)]
for c in s:
    d[ord(c) - ord('a')] += 1
for i in range(26):
    c = chr(ord('a') + i)
    l = -1
    r = -1
    cnt = 0
    for j in range(len(s)):
        if s[j] < c:
            l = j
        if s[j] == c:
            r = j
        if j - l >= m:
            if j - r >= m:
                cnt = -1
                break
            cnt += 1
            l = r
    if ~cnt:
        for k in range(i):
            print(chr(ord('a') + k) * d[k], end='')
        print(chr(ord('a') + i) * cnt)
        break
