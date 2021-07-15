from itertools import zip_longest

def six_column_encryption(msg, size=6):
    msg = msg.replace(' ','.')
    L = [msg[i:i+size] for i in range(0, len(msg), size)]
    return ' '.join(map(''.join, zip_longest(*L, fillvalue='.')))
