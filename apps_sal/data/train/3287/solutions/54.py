def mouth_size(x):
    x = x.lower()
    x = x.replace('!', '')
    return 'small' if x == 'alligator' else 'wide'
