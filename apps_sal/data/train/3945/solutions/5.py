def decipher_message(message):
    from math import sqrt
    if len(message) == 0:
        return message
    else:
        (lists, output) = ([], [])
        x = int(sqrt(len(message)))
        for i in range(0, len(message), x):
            lists.append(list(message[i:i + x]))
        for i in range(len(lists)):
            for j in range(len(lists)):
                output.append(lists[j][i])
        return ''.join(output)
