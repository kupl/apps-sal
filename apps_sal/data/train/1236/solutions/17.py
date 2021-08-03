t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    i = 1
    c = 0
    while i < n:
        if s[i] == s[i - 1]:
            c += 1
        i += 1
    print(c)
