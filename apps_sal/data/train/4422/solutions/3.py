def jumbled_string(s, n):
    ml = ['bullshit']
    new_str = s

    while s != ml[-1]:
        new_str = new_str[::2] + new_str[1::2]
        ml.append(new_str)
    return ml[n % (len(ml) - 1)]
