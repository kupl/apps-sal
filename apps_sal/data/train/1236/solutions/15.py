# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = str(input())
    lst = []
    c = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            pass
        else:
            c += 1
    print(c)
