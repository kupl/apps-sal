t = int(input())
for i in range(t):
    s = input().strip()
    x = 1
    a = 1000000007
    for j in range(len(s)):
        if s[j] == 'l' and j % 2 == 0:
            x = x * 2 % a
        elif s[j] == 'l' and j % 2 != 0:
            x = (x * 2 - 1) % a
        elif s[j] == 'r' and j % 2 == 0:
            x = (x * 2 + 2) % a
        else:
            x = (x * 2 + 1) % a
    print(x % a)
