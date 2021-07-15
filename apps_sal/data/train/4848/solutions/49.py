def char_freq(message):
    arr = []
    dict = {}
    for i in message:
        arr.append(i)
    for i in arr:    
        arr.count(i)
        dict[i] = arr.count(i)
    return dict
