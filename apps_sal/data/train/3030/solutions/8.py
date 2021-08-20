def nb_dig(n, d):
    string = ''
    count = 0
    for i in range(n + 1):
        string += str(i * i)
    for i in string:
        if i == str(d):
            count += 1
    return count
