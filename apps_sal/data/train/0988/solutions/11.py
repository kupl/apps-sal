for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    (x, cur_bit) = (0, 0)
    bitset = {}
    for ele in arr:
        while ele:
            if ele & 1:
                bitset[cur_bit] = bitset.get(cur_bit, 0) + 1
            cur_bit += 1
            ele >>= 1
        cur_bit = 0
    for b in bitset:
        if bitset[b] > n - bitset[b]:
            x |= 1 << b
    total = 0
    for ele in arr:
        total += ele ^ x
    print(total)
