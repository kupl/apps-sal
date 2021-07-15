from string import ascii_lowercase


def form_key(key):
    working_key = ""
    for letter in key + ascii_lowercase:
        if letter not in working_key:
            working_key += letter
    return working_key


def encode(msg, key, init_shift):
    encode_key = form_key(key)
    shift = init_shift
    encoded_msg = ""
    for letter in msg:
        if letter not in encode_key:
            encoded_msg += letter
        else:
            encoded_msg += encode_key[(encode_key.index(letter) + shift) % 26]
            shift = encode_key.index(letter) + 1
    return encoded_msg


def decode(msg, key, init_shift):
    decode_key = form_key(key)
    shift = init_shift
    decoded_msg = ""
    for letter in msg:
        if letter not in decode_key:
            decoded_msg += letter
        else:
            decoded_msg += decode_key[(decode_key.index(letter) - shift) % 26]
            shift = decode_key.index(decoded_msg[-1]) + 1
    return decoded_msg
