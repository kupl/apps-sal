S, L, x, y = set(), [], 0, 1
while not (x, y) in S:
    S.add((x, y))
    z = (x + y)%10
    L.append(z)
    x, y = y, z
memo = L[-2:] + L[:-2]

def get_last_digit(index):
    return memo[index % len(memo)]
