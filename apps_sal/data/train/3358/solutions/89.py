def correct(string):
    dic = {'5': 'S', '1': 'I', '0': 'O'}
    return ''.join([dic[x] if x in dic else x for x in list(string)])
