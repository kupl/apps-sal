def shorten_to_date(long_date):
    short=[]
    words = long_date.split(' ')
    for word in words:
        if word != words[2] and word != words[3]:
            short.append(word)
        elif word == words[2]:
            short.append(word[:-1])
    shortjoin = ' '.join(short)
    return shortjoin
