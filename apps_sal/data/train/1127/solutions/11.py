t = int(input())
for i in range(t):
    s = []
    s = input().split()
    for j in range(len(s)):
        s[j] = s[j].capitalize()
    for j in range(len(s) - 1):
        print(s[j][0], end='')
        print('.', end=' ')
    print(s[-1])
