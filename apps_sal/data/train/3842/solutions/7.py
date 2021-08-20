def word_wrap(text, limit):
    answer = []
    words = text.split()[::-1]
    line = ''
    while words:
        word = words.pop()
        if not line:
            if len(word) <= limit:
                line += word
            else:
                line += word[:limit]
                words.append(word[limit:])
        elif len(line) + 1 + len(word) <= limit:
            line += ' ' + word
        elif len(word) > limit:
            upto = limit - len(line) - 1
            line += ' ' + word[:upto]
            words.append(word[upto:])
        lenNext = len(words[-1]) if words else 0
        if not words or len(line) == limit or (lenNext <= limit and len(line) + 1 + lenNext > limit):
            answer.append(line)
            line = ''
    return '\n'.join(answer)
