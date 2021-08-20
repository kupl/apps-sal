from string import ascii_lowercase as a_low


def hamster_me(code, message):
    table = {}
    code = sorted(code)
    shift = a_low.index(code[0])
    abc = a_low[shift:] + a_low[:shift]
    for i in range(len(code)):
        start = abc.index(code[i])
        finish = abc.index(code[(i + 1) % len(code)])
        if finish == 0:
            finish = len(abc)
        ind = 1
        for j in abc[start:finish]:
            table[j] = code[i] + str(ind)
            ind += 1
    cipher = str.maketrans(table)
    return message.translate(cipher)
