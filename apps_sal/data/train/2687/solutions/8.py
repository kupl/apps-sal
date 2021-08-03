def format_words(words):
    if words != [""] and words != [] and words is not None:
        l = [word for word in words if word != '']
        return ", ".join(l[:-1]) + ' and ' + l[-1:][0] if len(l) > 1 else l[0]
    return ''
