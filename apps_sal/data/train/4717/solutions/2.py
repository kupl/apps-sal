def pattern(n):
    result = []
    for i in range(1, n + 1):
        nums = ''.join([str(j % 10) for j in range(1, i + 1)])
        result.append(' ' * (n - i) + nums + nums[::-1][1:] + ' ' * (n - i))
    return '\n'.join(result + result[::-1][1:])
