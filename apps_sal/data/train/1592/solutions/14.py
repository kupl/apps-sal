for _ in range(int(input())):
    chef = 0
    for j in range(int(input())):
        k = list(map(int, input().split()))
        if k[0] % 2 == 0:
            for r in range(1, k[0] // 2 + 1):
                chef += k[r]
        else:
            for r in range(1, k[0] // 2 + 2):
                chef += k[r]
    print(chef)
