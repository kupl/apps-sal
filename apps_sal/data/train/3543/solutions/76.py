def increment_string(strng):
    i = -1
    number = []
    if len(strng) == 0 or strng[i] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return strng + '1'
    while strng[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and i * -1 < len(strng):
        number.append(strng[i])
        i -= 1
    number.reverse()
    zero = len(number)
    if len(number) > 0:
        result = int(''.join(number)) + 1
    else:
        result = int(strng) + 1
    return strng[:-zero] + '0' * (len(number) - len(str(result))) + str(result)
