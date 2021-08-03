for t in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    dictionary = {0: 0}
    parity = 0
    k = 0
    for i in range(n):
        parity ^= (1 << c[i] - 1)
        if parity not in dictionary:
            dictionary[parity] = i + 1
        for j in range(30):
            x = parity ^ (1 << j)
            if x in dictionary:
                k = max(k, i - dictionary[x])

    print(k // 2)
