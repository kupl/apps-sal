import math


def optimalSol(a, b):
    power = int(math.log(a, 2))
    add = 0
    mod = 10**9 + 7
    previous_i = -1
    present = 0
    end = 0
    for i in range(power + 1):
        bit_add = 2**i
        end += 2**i
        if a & bit_add == bit_add:
            present += bit_add
            total_added = min(b - a + 1, end - present + 1)
            add += bit_add * total_added
    return add % mod


for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    print(optimalSol(a, b))
