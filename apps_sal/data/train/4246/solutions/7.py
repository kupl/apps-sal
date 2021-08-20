def covfefe(s):
    lst = list(s.split(' '))
    result = ['covfefe' if i == 'coverage' else i for i in lst]
    return ' '.join(result) if 'coverage' in lst else ' '.join(result) + ' covfefe'
