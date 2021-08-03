def correct(string):
    x = {'5': 'S', '0': 'O', '1': 'I'}
    return "".join(s if s not in x.keys() else x.get(s) for s in string)
