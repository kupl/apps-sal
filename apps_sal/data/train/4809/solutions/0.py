dict = {i[0]:i[1] for i in ['GA', 'DE', 'RY', 'PO', 'LU', 'KI', 'AG', 'ED', 'YR', 'OP', 'UL', 'IK','ga', 'de', 'ry', 'po', 'lu', 'ki', 'ag', 'ed', 'yr', 'op', 'ul', 'ik'] }
def encode(s):
    return ''.join([dict[i] if i in dict else i for i in s])
    
def decode(s):
    return ''.join([dict[i] if i in dict else i for i in s])

