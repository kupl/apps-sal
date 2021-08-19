def str_count(string, letter):
    # Your code here ;)
    count = 0
    if string == '':
        return 0
    else:
        for i in range(len(string)):
            if string[i] == letter:
                count = count + 1
    return count
