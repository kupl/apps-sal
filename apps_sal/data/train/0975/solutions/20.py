for _ in range(int(input())):
    n, r, x, y = [int(x) for x in input().split()]
    repeat = []
    plagis = []
    if x > 0:
        repeat = [int(x) for x in input().split()]
    if y > 0:
        plagis = [int(x) for x in input().split()]
    invalid = set(repeat).union(set(plagis))
    print(min(r, n - len(invalid)))
