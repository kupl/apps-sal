def encode(message, key):
    key = list(str(key) * (len(message) // len(str(key)) + 1)) if len(str(key)) < len(message) else list(str(key))
    encode_list = []
    key_index = 0
    for i in list(message):
        encode_list.append(ord(i) - 96 + int(key[key_index]))
        key_index += 1
    return encode_list
