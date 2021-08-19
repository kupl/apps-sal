def correct(m, n, bits):
    res = []
    for i in range(0, n * m, n):
        res.append(bits[i:i + n])
    start = n * m
    check = []
    check.append(next((i for i in range(m) if digit_sum(res[i]) % 2 != int(bits[start + i])), None))
    for j in range(n):
        string = ''
        for i in range(m):
            string += res[i][j]
        if digit_sum(string) % 2 != int(bits[start + m + j]):
            check.append(j)
            break
    if len(check) == 1:
        check.append(None)
    if check[0] == None and check[1] == None:
        return bits
    elif check[1] == None:
        temp = '0' if bits[start + check[0]] == '1' else '1'
        return bits[:start + check[0]] + temp + bits[start + check[0] + 1:]
    elif check[0] == None:
        temp = '0' if bits[start + m + check[1]] == '1' else '1'
        return bits[:start + m + check[1]] + temp + bits[start + m + check[1] + 1:]
    else:
        temp = '0' if res[check[0]][check[1]] == '1' else '1'
        return bits[:check[0] * n + check[1]] + temp + bits[check[0] * n + check[1] + 1:]


def digit_sum(s):
    return sum((int(i) for i in s))
