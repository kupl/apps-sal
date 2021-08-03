# python3
def solve():
    for __ in range(int(input())):
        p, q, b = tuple(map(int, input().split()))
        yield "Infinite" if p * pow(b, 63, q) % q else "Finite"


print("\n".join(solve()))
