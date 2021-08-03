for _ in range(int(input())):
    n = int(input())
    if(n == 1):
        print(0)
    else:
        print(pow(2, n - 1, 10**9 + 7) - 2)
