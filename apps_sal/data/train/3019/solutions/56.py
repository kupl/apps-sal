def str_count(string, letter):
    count = 0
    for c in string:
        if letter == c:
            count += 1
    return count
