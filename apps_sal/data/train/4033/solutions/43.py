def contamination(text, char):
    if text is '' or char is '':
        return ''
    else:
        return char * len(text)
