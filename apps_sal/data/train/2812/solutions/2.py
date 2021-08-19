def pattern(n):
    result = []
    if n == 1:
        return ''
    for i in range(n + 1):
        if i % 2 == 0:
            result.append(str(i) * i + '\n')
    return ''.join(result).strip()
