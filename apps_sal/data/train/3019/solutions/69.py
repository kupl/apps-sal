def str_count(string, letter):
    counter = 0
    for i in string:
        if i == letter:
            counter = counter + 1
    return counter
