def tops(msg):
    if not msg:
        return ''
    (n, length) = (2, len(msg))
    counter = 0
    s = ''
    while counter + n <= length:
        counter += n
        s += msg[counter - 1]
        counter += n - 1
        n += 2
    return s[::-1]
