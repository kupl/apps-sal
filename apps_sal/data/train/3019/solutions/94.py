def str_count(string, letter):
    count = 0
    for i in range(len(string)):
        if letter in string[i]:
            count += 1
    return count
