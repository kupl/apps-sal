def char_freq(message):
    str_ = {}

    for i in message:
        if i in str_:
            str_[i] += 1
        else:
            str_[i] = 1

    return str_
