def char_freq(string):
    my_dict = {}
    for s in string:
        n = string.count(s)
        my_dict[s] = n

    return my_dict
