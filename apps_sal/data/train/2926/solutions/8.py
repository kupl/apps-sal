def reverse(a):
    reversed_str = "".join(a)[::-1]
    final_arr = []
    start = 0
    finish = len(a[0])
    for i in range(1, len(a) + 1):
        final_arr.append(reversed_str[start:finish])
        start = finish
        if len(a) > i:
            finish = start + len(a[i])

    return final_arr
