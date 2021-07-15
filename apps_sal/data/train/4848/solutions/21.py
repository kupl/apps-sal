def char_freq(message):
    dic = {}
    for each in message:
        try:
            if dic[each]:
                dic[each] += 1
        except KeyError:
            dic[each] = 1
    return(dic)
