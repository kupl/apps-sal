for _ in range(int(input())):
    n, k, l = map(int, input().split())
    if(n > k * l or (n > 1 and k == 1) or n <= 0):
        print("-1")
    else:
        temp = 1
        for i in range(0, n):
            print(temp, end=" ")
            temp = (temp + 1) % k
            if(temp == 0):
                temp = k
        print()
