for _ in range(int(input())):
    x = 0
    for c in range(int(input())):
        n, m = map(int, input().split())
        g = (m + n - 2) % 3
        x = x ^ g
    if x:
        print("MasterChef")
    else:
        print("Football")
