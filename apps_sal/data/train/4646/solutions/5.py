def encode(s):
    return ''.join([[i, '10'[ord(i) % 2]][i.isalpha()] for i in s ])
