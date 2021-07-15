def split_odd_and_even(n):
    new_n = ''
    for c in str(n):
        if not new_n or not (int(new_n[-1]) - int(c)) % 2:
            new_n += c
        else :
            new_n += '.'+c
    return [int(i) for i in new_n.split('.')]
