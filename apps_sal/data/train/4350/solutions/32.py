def pre_fizz(n):
    new_arr = []
    while n > 0:
        new_arr.append(n)
        n -= 1
        new_arr.sort()
    return new_arr
