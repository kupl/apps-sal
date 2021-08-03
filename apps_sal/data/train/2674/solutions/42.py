def two_sort(array):
    ans = ''
    array.sort()
    for i in array[0]:
        ans = ans + (i + '***')
    return ans[0:-3]
