# cook your dish here

arr = [[0 for i in range(101)] for i in range(101)]
for i in range(1, 100):
    k = 0
    for j in range(i + 1, 101):
        arr[i][j] = k
        k = 1 - k
        arr[j][i] = k

t = int(input())
while t:
    n = int(input())
    if n % 2 == 0:
        print("NO")
    else:
        print("YES")
        a = [arr[i][-n:] for i in range(-n, 0)]
        for i in range(0, n):
            print(*a[i], sep='')
    t -= 1
