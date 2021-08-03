# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    s = ""
    for i in range(1, n + 1):
        if i % 2 != 0:
            s += '1'
        else:
            s += '0'
    for i in range(1, n + 1):
        print(s)
