def decode(string):
    cipher_map = {'0': '5', '1': '9', '2': '8', '3': '7', '4': '6', '5': '0', '6': '4', '7': '3', '8': '2', '9': '1'}
    return ''.join([cipher_map[s] for s in string])
