def word_wrap(text, limit):
    words = text.split(' ')
    current = 0
    for i in range(len(words)):
        word = words[i]
        prev = current
        current += len(word) + 1
        if current - 1 == limit:
            words[i] += ' '
            current = 0
        elif current > limit:
            if len(word) > limit:
                j = 0
                while current > limit:
                    j += limit - prev
                    current = len(word) - j
                    words[i] = word[:j] + '  ' + word[j:]
                    word = words[i]
                    j += 2
                    prev = 0
                current += 1
            else:
                words[i - 1] += ' '
                current = len(word) + 1 if i < len(words) - 1 else len(word)
                if current == limit:
                    words[i] += ' '
                    current = 0
    return ' '.join(words).replace('  ', '\n').strip()
