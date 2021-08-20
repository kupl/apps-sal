from itertools import cycle


def de_nico(key, msg):
    code = tuple((sorted(key).index(k) + 1 for k in key))
    code_cycle = cycle(code)
    key_cycle = cycle(range(1, len(key) + 1))
    msg_encrypted = [(k, next(key_cycle)) for k in msg]
    result = []
    while msg_encrypted:
        try:
            index = next(code_cycle)
            found = next((p for p in msg_encrypted if p[1] == index))
            msg_encrypted.remove(found)
            result.append(found[0])
        except StopIteration:
            pass
    return ''.join(result).strip()
