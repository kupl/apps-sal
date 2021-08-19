for _ in range(int(input())):
    n = int(input())
    s = list(input())
    result = [0] * n
    ones = []
    zeroes = []
    current = 1
    for i in range(n):
        if s[i] == '0':
            if len(zeroes) == 0:
                ones.append(current)
                result[i] = current
                current += 1
            else:
                x = zeroes.pop()
                result[i] = x
                ones.append(x)
        elif len(ones) == 0:
            zeroes.append(current)
            result[i] = current
            current += 1
        else:
            x = ones.pop()
            result[i] = x
            zeroes.append(x)
    print(current - 1)
    print(*result)
