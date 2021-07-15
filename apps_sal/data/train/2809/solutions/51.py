def digitize(n):
    str_arr = list(str(n)[::-1])
    int_arr = []
    for i in str_arr:
        int_arr.append(int(i))
    return int_arr
