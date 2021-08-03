def char_freq(message):
    arr = [*message]
    _dict = {}

    for i in arr:
        _dict[i] = _dict.get(i, 0) + 1

    return _dict
