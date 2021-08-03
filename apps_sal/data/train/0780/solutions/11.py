for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    print(["EVEN", "ODD"][(n % m) & 1])
