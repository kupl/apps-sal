def char_freq(message):
    my_dict = {}
    for i in message:
        my_dict[i] = my_dict.get(i, 0) + 1
    return my_dict
