for i in range(int(input())):
    n, k = map(int, input().split())
    isproductsatisfied = (n * k % 2 == 0)
    print("YES" if isproductsatisfied else "NO")
