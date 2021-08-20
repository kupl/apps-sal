def list_squared(m, n):
    ans = []
    sum = 0
    for i in range(m, n + 1):
        sq = int(i ** 0.5)
        if sq > 1 and sq == i ** 0.5:
            sq -= 1
        for j in range(1, sq + 1):
            if i % j == 0:
                if j != int(i / j):
                    sum += j ** 2 + int(i / j) ** 2
                else:
                    sum += j ** 2
        if sum > 0 and sum ** 0.5 % 1 == 0:
            ans.append([i, sum])
        sum = 0
    return ans
