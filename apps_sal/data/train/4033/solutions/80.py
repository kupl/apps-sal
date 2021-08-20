def contamination(text, char):
    return text.replace(text, char * len(text))


print(contamination('_3ebzgh4', '&'))
