t = int(input())
for i in range(t):
    n = int(input())
    s = input()  # qwert 01234
    c = 0
    for j in range(n):
        if(j + 1 < n):
            if(s[j] == s[j + 1]):
                c = c + 1
    print(c)
