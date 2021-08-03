# cook your dish here
for _ in range(int(input())):
    n, d = input().split()
    s = list(n)
    l = list(n)
    prev = d
    k = 0
    for x in range(len(l) - 1, -1, -1):
        if n[x] > prev:
            s[x] = ''
            k += 1
        else:
            prev = s[x]

    s = ''.join(s) + d * k
    print(s)
