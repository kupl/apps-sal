s = int(input())
b = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
for _ in range(s):
    v = 0
    y = int(input())
    i = 0
    while y:
        v += y // b[i]
        y = y % b[i]
        i = i + 1
    print(v)
