def str_count(string, letter):
    result = 0
    for i in string:
        if i == letter:
            result += 1
    return result
