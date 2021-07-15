def men_from_boys(arr):
    odd_arr = []
    eve_arr = []
    for i in arr:
        if i % 2 and i not in odd_arr:
            odd_arr.append(i)
        if not i % 2 and i not in eve_arr:
            eve_arr.append(i)
    eve_arr.sort()
    odd_arr.sort(reverse=True)
    return eve_arr + odd_arr
