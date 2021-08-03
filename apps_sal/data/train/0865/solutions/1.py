for _ in range(int(input())):
    n = int(input())
    print(0) if(n == 1) else print(pow(2, n - 1, 10**9 + 7) - 2)
