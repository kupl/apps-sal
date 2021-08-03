def find_the_key(msg, code):
    from itertools import cycle
    msg = [ord(i) - 96 for i in msg]
    keys = [code[i] - msg[i] for i in range(len(code))]
    key = ''.join([str(i) for i in keys])

    i = 1
    while True:
        a = cycle(key[:i])
        if [_ + int(next(a)) for _ in msg] == code:
            return int(key[:i])
        else:
            i += 1
