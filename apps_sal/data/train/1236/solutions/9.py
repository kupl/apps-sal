t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    s = list(s)
    c = 0
    for j in range(len(s) - 1):
        if(s[j] == s[j + 1]):
            c = c + 1
    print(c)
