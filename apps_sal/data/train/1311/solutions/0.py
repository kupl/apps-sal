test = int(input())
for i in range(test):
    n, k = map(int, input().split())
    x = n - k
    for j in range(1, n + 1):
        if(j % 2 == 0 and x > 0):
            print(-j, end=' ')
            x -= 1
        elif(k <= 0):
            print(-j, end=' ')
        else:
            print(j, end=' ')
            k -= 1
    print()
