t = int(input())

for t1 in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = bin(a[0])[2:]
    s1 = a[0]
    for i in range(1, n):
        x = bin(a[i])[2:]

        if len(s) > len(x):
            j = 1
            s1 = ''
            while j <= len(x):
                if s[-j] == x[-j]:
                    s1 += "0"
                else:
                    s1 += "1"
                j += 1

            while j <= len(s):
                s1 += s[-j]
                j += 1

            s = s1[::-1]
        else:
            j = 1
            s1 = ''
            while j <= len(s):
                if s[-j] == x[-j]:
                    s1 += "0"
                else:
                    s1 += "1"
                j += 1

            while j <= len(x):
                s1 += x[-j]
                j += 1

            s = s1[::-1]

    s = "0b" + s
    print(int(s, 2))
