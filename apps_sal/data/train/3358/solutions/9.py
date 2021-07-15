def correct(string):
    tr = {'0': 'O', '1' : 'I', '5':'S'}
    return ''.join([tr[i] if i.isdigit() else i for i in string])
