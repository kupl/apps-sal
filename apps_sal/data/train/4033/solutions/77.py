def contamination(text, char):
    if text:
        return ''.join([char for el in list(text)])
    else:
        return ''
