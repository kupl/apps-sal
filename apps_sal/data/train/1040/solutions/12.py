t = int(input())
while t > 0:
    (x, q) = input().split()
    x = int(x)
    q = int(q)
    s = input()
    list = []
    list.append(0)
    list.append(0)
    sum = 0
    ptr = 0
    for i in s:
        if ptr + 2 > len(s) - 1:
            break
        else:
            a = s[ptr]
            b = s[ptr + 1]
            c = s[ptr + 2]
            if (a == b) | (b == c) | (a == c):
                sum += 1
            list.append(sum)
            ptr += 1
    while q > 0:
        (l, r) = input().split()
        l = int(l)
        r = int(r)
        if r - l < 2:
            print('NO')
        else:
            res = list[r - 1] - list[l]
            if res > 0:
                print('YES')
            else:
                print('NO')
        q -= 1
    t -= 1
