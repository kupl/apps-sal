t = int(input())
for _ in range(t):
    n = input()
    y = [int(x) for x in n]
    z = sum(y)
    if z < 5 and len(y) > 1:
        print(9 - z)
    else:
        print(min(z % 9, 9 - z % 9))
