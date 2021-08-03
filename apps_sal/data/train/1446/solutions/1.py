# cook your dish here
t = int(input())
s = []
for i in range(31):
    s.append(2**i - 1)
for _ in range(t):

    n = int(input())

    if n == 1:
        print(2)
    else:
        if n in s:
            print(n // 2)
        else:
            print(-1)
