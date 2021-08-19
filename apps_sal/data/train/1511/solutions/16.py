from collections import deque
t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    s = input()
    l = str()
    for i in range(n):
        if s[i] == ':':
            l += ':'
        l += s[i]
    fe = deque()
    mg = deque()
    tot = 0
    for i in range(len(s)):
        if s[i] == 'I':
            while len(mg) > 0 and abs(mg[0] - i) > k:
                mg.popleft()
            if len(mg) > 0:
                tot += 1
                mg.popleft()
            else:
                fe.append(i)
        elif s[i] == 'M':
            while len(fe) > 0 and abs(fe[0] - i) > k:
                fe.popleft()
            if len(fe) > 0:
                tot += 1
                fe.popleft()
            else:
                mg.append(i)
        elif s[i] == 'X':
            while len(fe) > 0:
                fe.popleft()
            while len(mg) > 0:
                mg.popleft()
    print(tot)
