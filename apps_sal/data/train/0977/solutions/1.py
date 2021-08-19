for _ in range(int(input())):
    n = int(input())
    l = list(map(str, input()))
    k = n
    if n % 2 != 0:
        k = n - 1
    for i in range(0, k, 2):
        (l[i], l[i + 1]) = (l[i + 1], l[i])
    for i in range(n):
        a = ord(l[i]) - 97
        a = 122 - a
        l[i] = chr(a)
    for i in range(n):
        print(l[i], end='')
    print()
