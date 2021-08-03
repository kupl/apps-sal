def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def encode(message, key, initShift):
    new_key = ''
    for i in key:
        if i not in new_key:
            new_key += i

    alf = 'abcdefghijklmnopqrstuvwxyz'
    for i in alf:
        if not i in new_key:
            new_key += i

    alphabet = {x: y for x, y in zip(range(1, 27), new_key)}
    result = ''
    for i in message:
        if i.isalpha() == False:
            result += i
            continue
        i = get_key(alphabet, i)
        if (i + initShift) <= 26:
            result += alphabet.get(i + initShift)
            initShift = i
        else:
            result += alphabet.get((i + initShift) - 26)
            initShift = i
    return result


def decode(message, key, initShift):
    new_key = ''
    for i in key:
        if i not in new_key:
            new_key += i

    alf = 'abcdefghijklmnopqrstuvwxyz'
    for i in alf:
        if not i in new_key:
            new_key += i

    alphabet = {x: y for x, y in zip(range(1, 27), new_key)}
    result = ''
    for i in message:
        if i.isalpha() == False:
            result += i
            continue
        i = get_key(alphabet, i)
        if (i - initShift) > 0:
            result += alphabet.get(i - initShift)
            initShift = i - initShift
        elif (i - initShift + 26) == 0:
            result += alphabet.get(26)
            initShift = 26
        else:
            result += alphabet.get((i - initShift) + 26)
            initShift = (i - initShift) + 26
    return result
