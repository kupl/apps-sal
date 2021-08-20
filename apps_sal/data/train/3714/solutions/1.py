def encoder(data):

    def get_key_by_value(value):
        for key in dictionary:
            if dictionary[key] == value:
                return key
    dictionary = {0: ''}
    dict_index = 1
    substring = ''
    encoded = []
    for char in data:
        substring += char
        if substring not in list(dictionary.values()):
            dictionary[dict_index] = substring
            encoded.append(str(get_key_by_value(substring[:-1])))
            encoded.append(substring[-1])
            dict_index += 1
            substring = ''
    if substring != '':
        encoded.append(str(get_key_by_value(substring)))
    return ''.join(encoded)


def decoder(data):
    dictionary = {0: ''}
    dict_index = 1
    decoded = []
    key = ''
    for char in data:
        if char.isdigit():
            key += char
        else:
            substring = dictionary[int(key)] + char
            dictionary[dict_index] = substring
            dict_index += 1
            decoded.append(substring)
            key = ''
    if key != '':
        decoded.append(dictionary[int(key)])
    return ''.join(decoded)
