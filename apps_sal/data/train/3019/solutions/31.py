def str_count(string, letter):
    count = 0
    for l in string:
        if letter == l:
            count += 1
    return count
