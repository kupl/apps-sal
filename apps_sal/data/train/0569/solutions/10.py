import math


def solve(N):
    bucket = math.ceil((math.sqrt(8 * N + 1) - 1) // 2)
    return N - (bucket * bucket + bucket) // 2


T = int(input())
for _ in range(T):
    N = int(input())
    result = solve(N)
    print(result)
