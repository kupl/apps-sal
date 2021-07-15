def format_words(words):
    if not words or words == ['']:
        return ''
    words = [i for i in words if i != '']
    if len(words) == 1:
        return words[0]
    return ', '.join(words[:-1]) + ' and ' + words[-1]
