# cook your dish here
for _ in range(int(input())):
    n = int(input())
    m = n
    x = 1
    for i in range(n):
        for j in range(m):
            print(x, end='')
            x += 1
        print()
        m -= 1
