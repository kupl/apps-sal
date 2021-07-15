def get_near_power_of_two(x):
    b = 1
    while b <= x:
        b <<= 1
    return b >> 1

n = int(input())
for _ in range(n):
    l, r = list(map(int, input().split()))
    xor = l ^ r
    d = get_near_power_of_two(xor) - (0 if xor == 0 else 1)
    ld = l | d
    rd = r | d
    print(rd if rd == r else ld)

