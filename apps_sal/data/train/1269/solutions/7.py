t = int(input())
for i in range(t):
    n = int(input())
    sum = 0
    a = sorted((list(map(int, input().split()))))
    b = sorted((list(map(int, input().split()))))
    for j in range(n):
        if(a[j] < b[j]):
            sum += a[j]
        else:
            sum += b[j]
    print(sum)
