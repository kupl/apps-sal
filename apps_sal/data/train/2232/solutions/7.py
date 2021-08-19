def solve(x):
    return ((x + 1) ** 2 * x ** 2 - (x * x - x)) / x


inp = int(input(''))
lvl = 1
print('2')
while inp >= 2:
    ops = solve(lvl + 1)
    print(int(ops))
    lvl = lvl + 1
    inp = inp - 1
