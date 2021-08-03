def encode(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    letters_numbers = {}
    for i in range(len(alphabet)):
        dict_ = {alphabet[i]: i + 1}
        letters_numbers.update(dict_)
    message_numbers = []
    for j in message:
        number = letters_numbers[j]
        message_numbers.append(number)
    key = str(key)
    key = list(key)
    final_message_encoded = []
    for k in range(len(message)):
        key.append(key[k])
    for l in range(len(message_numbers)):
        message_encoded = message_numbers[l] + int(key[l])
        final_message_encoded.append(message_encoded)
    return final_message_encoded
