n = int(input())

for i in range(n):
    l, r = list(map(int, input().split()))
    bits = 0
    result = 0
    while True:
        count_bit = len(str(bin(r))) - 2
        if (1 << count_bit) - 1 == r:
            result += (1 << count_bit) - 1
            break
        exp = (1 << (count_bit - 1)) - 1
        if exp >= l:
            result += exp
            break
        else:
            bits += 1
            exp = 1 << (count_bit - 1)
            result += exp
            l -= exp
            r -= exp
    print(result)
