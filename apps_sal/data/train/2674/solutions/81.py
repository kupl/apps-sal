def two_sort(array):
    return ''.join([x + '***' for x in sorted(array)[0]]).strip('*')
