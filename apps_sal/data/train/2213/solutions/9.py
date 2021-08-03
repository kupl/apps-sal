for _ in range(int(input())):
    a, b, n = [int(i) for i in input().split()]
    print([a, b, a ^ b][n % 3])
