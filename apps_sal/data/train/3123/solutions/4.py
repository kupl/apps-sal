def count_repeats(string):

    temp = ""
    count = 0
    for i in list(string):
        if i == temp:
            count += 1
        temp = i

    return count
