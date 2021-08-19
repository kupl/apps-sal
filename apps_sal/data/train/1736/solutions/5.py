def is_interesting(number, awesome_phrases):
    for (r, num) in zip((2, 1, 1), range(number, number + 3)):
        num_str = str(num)
        if num in awesome_phrases or (num > 99 and (int(num_str[1:]) == 0 or num_str[::-1] == num_str or num_str in '1234567890' or (num_str in '9876543210'))):
            return r
    return 0
