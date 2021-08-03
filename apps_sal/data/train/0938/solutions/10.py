for _ in range(eval(input())):
    n = eval(input())
    l = list(map(int, input().split()))
    c = 0
    s = []
    for i in range(n):
        for j in range(i, n):
            s += [set(l[i:j + 1])]
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            c += len(s[i] & s[j]) == 0
    print(c)
