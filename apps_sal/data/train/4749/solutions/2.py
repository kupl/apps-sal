def base_finder(seq):
    base = 0
    for i in range(10):  # as the sequence will always be 10 numbers long
        number = seq[i]  # converting each list element to a string
        for i in range(len(number)):
            if int(number[i]) > base:  # Comparing each character of string to base
                base = int(number[i])  # updating the base value
    return base + 1  # return base value
