def correct(string):
    for (e, c) in {'5': 'S', '0': 'O', '1': 'I'}.items():
        string = string.replace(e, c)
    return string
