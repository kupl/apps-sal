def x(n):
    result = []
    for i in range(int(n / 2) + 1):
        line = '□' * i + '■' + '□' * (int(n / 2) - i)
        result.append(line + line[::-1][1:])
    return '\n'.join(result + result[::-1][1:])
