t = int(input())
for tc in range(t):
    n = int(input())
    s = input()
    l = 0
    for j in range(1, n):
        if s[j] == s[j - 1]:
            l = l + 1
    print(l)
