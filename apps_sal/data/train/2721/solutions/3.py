def pyramid(n):

    result = ''
    for i in range(n - 1):
        result += ' ' * (n - i - 1) + '/' + ' ' * i * 2 + '\\\n'
    result += '/' + '_' * 2 * (n - 1) + '\\\n'
    print(result)
    return result
