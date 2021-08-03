def encode(message, key):
    pre_output = []
    for letter in message:
        pre_output.append(ord(letter) - 96)
    output = []
    key = str(key)
    i = 0
    for number in pre_output:
        output.append(number + int(key[i]))
        if i == len(key) - 1:
            i = 0
        else:
            i += 1
    return output
