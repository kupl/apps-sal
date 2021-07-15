def decipher_this(string):
    translated = []
    for word in string.split():
        digits = ''
        for c in word:
            if c.isdigit():
                digits += c
        word = word.replace(digits, chr(int(digits)))    
        if len(word) > 2:
            translated.append(''.join([word[0], word[-1], word[2:-1], word[1]]))
        else:
            translated.append(word)
    return ' '.join(translated)
