t = int(input())
for q in range(t):
    n = int(input())
    s = input()
    l = list(s)
    for i in range(0, n, 2):
        if i == n - 1:
            continue
        t = l[i]
        l[i] = l[i + 1]
        l[i + 1] = t
    for i in l:
        print(chr(122 - ord(i) + 97), end='')
    print()
