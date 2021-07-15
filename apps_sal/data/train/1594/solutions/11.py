t = int(input())

while t > 0:
    n = int(input())
    a = []
    for i in range(n):
        temp = input()
        a.append(temp)

    print((n*n+n)//2)
    t-=1
