def mul3(ip):
    q0 = []
    q1 = []
    q2 = []
    ip.sort()
    sums = sum(ip)
    for i in ip:
        if i % 3 == 0:
            q0.insert(0, i)
        if i % 3 == 1:
            q1.insert(0, i)
        if i % 3 == 2:
            q2.insert(0, i)
    if sums % 3 == 1:
        if len(q1):
            q1.pop()
        elif len(q2) >= 2:
            q2.pop()
            q2.pop()
        else:
            return -1
    elif sums % 3 == 2:
        if len(q2):
            q2.pop()
        elif len(q1) >= 2:
            q1.pop()
            q1.pop()
        else:
            return -1
    q0.extend(q1)
    q0.extend(q2)
    if len(q0) <= 0:
        return -1
    q0.sort()
    q0.reverse()
    return q0


t = int(input())
for z in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if 0 not in a or mul3(a) == -1:
        print(-1)
    else:
        out = ''
        temp = mul3(a)
        for p in temp:
            out += str(p)
        print(out)
