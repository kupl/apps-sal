def shorten_to_date(long_date):
    x = []
    for i in range(len(long_date)):
        if long_date[i] == ",":
            break
        x.append(long_date[i])
    s = ''.join(x)
    
    return s
