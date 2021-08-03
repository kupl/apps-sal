for _ in range(int(input())):
    a, b, n = (int(s) for s in input().split())
    l = [a, b, a ^ b]
    print(l[n % 3])
