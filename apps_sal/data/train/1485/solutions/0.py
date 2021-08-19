# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l1 = []
    l2 = []

    for i in range(n):
        s = input()
        a = s[:n // 2].count('1')
        b = s[n // 2:].count('1')
        if a > b:
            l1.append(a - b)

        elif a < b:
            l2.append(b - a)

    p = sum(l1)
    q = sum(l2)

    if p == q:
        print(0)

    elif p > q:
        diff = p - q
        flag = 0
        for i in range(diff // 2, 0, -1):
            a = diff - i
            if (i in l1) or (a in l1):
                print(abs(a - i))
                flag = 1
                break

        if flag == 0:
            print(diff)

    else:
        diff = q - p
        flag = 0
        for i in range(diff // 2, 0, -1):
            a = diff - i
            if (i in l2) or (a in l2):
                print(abs(a - i))
                flag = 1
                break

        if flag == 0:
            print(diff)
