def two_sort(array):
    new_arr = sorted(array)
    final_arr = []
    for x in new_arr[0]:
        x += '***'
        final_arr.append(x)
    word = ''.join(final_arr)
    return word.strip('***')
