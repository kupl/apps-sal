t = int(input())
while(t > 0):
    n, k = map(int, input().split())
    cnt = n / 2
    diff = n - k

    if(k > cnt):
        for i in range(1, n + 1):
            if(diff > 0 and i % 2 == 1):
                diff -= 1
                print(-i, end=" ")
            else:
                print(i, end=" ")

    else:
        for i in range(1, n + 1):
            if(k > 0 and i % 2 == 0):
                k = k - 1
                print(i, end=" ")
            else:
                print(-i, end=" ")

    print()
    t = t - 1
