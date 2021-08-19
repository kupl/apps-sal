def next_numb(val):
    i = val + 1
    while i <= 9999999999:
        if i % 3 == 0 and i % 2 and (len(str(i)) == len(set(str(i)))):
            return i
        i += 1
    return 'There is no possible number that fulfills those requirements'
