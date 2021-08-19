# cook your dish here
t = int(input())
for i in range(0, t):
    n, k = [int(n) for n in input().split()]
    a = input().split()
    b = []
    for j in range(0, k):
        x = input().split()
        for p in range(1, len(x)):
            b.append(x[p])
    r = 0
    for r in range(0, len(a)):
        if b.__contains__(a[r]):
            print('YES', end=" ")
        else:
            print("NO", end=" ")
    print(" ")
