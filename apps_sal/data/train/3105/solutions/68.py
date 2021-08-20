def count_sheep(n):
    count = ''
    for i in range(1, n + 1):
        count += str(int(i)) + ' sheep...'
    return count
