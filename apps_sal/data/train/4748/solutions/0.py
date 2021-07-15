def insert_dash2(num):
    
    prev = 0
    out = ''

    for dig in str(num):
        if int(dig) % 2 == int(prev) % 2 and int(prev) and int(dig):
            out += '*-'[int(prev) % 2]
        out += dig
        prev = dig
    return out
