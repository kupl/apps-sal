for _ in range(int(input())):
    n = int(input())
    result = n ** 3 + (n - 1) ** 2
    result = result % 1000000007
    print(result)
