def format_words(words):
    words = [w for w in words if w] if words else ''
    if not words:
        return ''
    return '{seq} and {last}'.format(seq=', '.join(words[:-1]), last=words[-1]) if len(words) !=1 else '{0}'.format(words[0])
