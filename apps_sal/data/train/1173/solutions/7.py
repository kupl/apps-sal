import math

for _ in range(int(input())):
    N = int(input())
    Arr = [int(o) for o in input().split()]
    res = 0
    xor_array = [0] * 1000000
    length = [0] * 1000000
    x = [0] * 1000000
    xor_val = 0
    xor_array[0] = 1
    x[0] = -1
    for i in range(N):
        cnt = 0
        xor_val = xor_val ^ Arr[i]
        if xor_array[xor_val]:
            cnt = i - x[xor_val]
            length[xor_val] = length[xor_val] + ((xor_array[xor_val] * cnt) - 1)
            res += length[xor_val]
        x[xor_val] = i
        xor_array[xor_val] += 1
    print(res)
