def two_sort(array):
    return '***'.join(sorted(array)[0][i]for i in range(len(sorted(array)[0])))
