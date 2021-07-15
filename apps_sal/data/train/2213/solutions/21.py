for cas in range(int(input())):
    x, y, z = map(int, input().split())
    print([x, y, x ^ y][z % 3])
