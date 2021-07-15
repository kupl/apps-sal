def char_freq(message):
    
    print(message)

    d = dict()
    for c in message:
        d[c] = d.get(c,0) + 1
    
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[0]))
    
    return sorted_dict
