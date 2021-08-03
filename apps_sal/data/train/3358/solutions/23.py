def correct(string):
    return ''.join([({'0': 'O', '5': 'S', '1': 'I'}[ch] if ch in ['5', '0', '1'] else ch) for ch in string])
