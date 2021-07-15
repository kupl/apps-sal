def str_count(strng, letter):
    letter_count = 0
    for i in strng:
        if i == letter:
            letter_count += 1
    return letter_count
