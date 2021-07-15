from itertools import zip_longest

def six_column_encryption(msg):
    return ' '.join(map(''.join,
        zip_longest(*(msg[i:i+6].replace(' ', '.') for i in range(0, len(msg), 6)), fillvalue='.')
    ))
