for i in range(eval(input())):
    (n, k) = input().strip().split()
    n = int(n)
    k = int(k)
    print(int(n - k & int((k - 1) / 2) == 0))
