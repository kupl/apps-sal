from string import ascii_lowercase as al

def find_the_key(message, code):
    msg_key = ''.join([str(a - d) for (a, d) in zip(code, [al.index(c) + 1 for c in message])])
    key, len_msg = '', len(msg_key)
    for i, n in enumerate(msg_key, 1):
        key += n
        d, m = divmod(len_msg, i)
        test_key = key * (d + (m > 0))  # round up integer without math.ceil
        if test_key[:len_msg] == msg_key:
            return int(key)
