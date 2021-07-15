def hex_hash(code):
    first = ''
    for i in code :
        first += hex(ord(i))[2:]
    second = ''
    for i  in first :
        if i.isdigit() :
            second += i
    last = 0
    for i in second:
        last += int(i)
    return last
