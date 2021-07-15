def vowel_shift(text, n):
    if text is None or text is '':
        return text
    text = [n for n in text]
    vowels = []
    for x in range(len(text)):
        if text[x].lower() in 'aeuoi':
            vowels.append(text[x])
            text[x] = None
    if len(vowels) == 0:
        return ''.join(text)
    while n != 0:
        if n > 0:
            vowels.insert(0, vowels.pop(-1))
            n -= 1
        else:
            vowels.insert(len(vowels) - 1, vowels.pop(0))
            n += 1
    while len(vowels) != 0:
        text[text.index(None)] = vowels.pop(0)
    return ''.join(text)
