s = input()
t = input()
n = len(s)
m = len(t)
sl = [0]
for i in s:
    sl.append(sl[-1])
    if i == "A":
        sl[-1] += 1
    else:
        sl[-1] += 2
    sl[-1] %= 3
tl = [0]
for i in t:
    tl.append(tl[-1])
    if i == "A":
        tl[-1] += 1
    else:
        tl[-1] += 2
    tl[-1] %= 3
q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    a -= 1
    c -= 1
    ss = sl[b] - sl[a]
    tt = tl[d] - tl[c]
    if ss % 3 == tt % 3:
        print("YES")
    else:
        print("NO")
