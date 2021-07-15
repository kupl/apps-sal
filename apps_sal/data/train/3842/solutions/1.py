def word_wrap(text, limit):
    result = []
    s = ''
    for word in text.split():
        if len(word) > limit:
            if len(s) + 1 >= limit:
                result.append(s)
                s = ''
            if s:
                s += ' '
            i = limit - len(s)
            result.append(s + word[:i])
            for j in range(i, len(word) + 1, limit):
                s = word[j:j + limit]
                if len(s) == limit:
                    result.append(s)
        elif len(word) == limit:
            if s:
                result.append(s)
                s = ''
            result.append(word)
        elif len(word) + len(s) + 1 > limit:
            result.append(s)
            s = word
        else:
            s += ' ' + word if s else word
    if s:
        result.append(s)
    return '\n'.join(result)
