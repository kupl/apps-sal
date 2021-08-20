def capitalize_word(word):
    final = ''
    pos = 0
    while pos < len(word):
        if pos == 0:
            final += word[pos].upper()
        else:
            final += word[pos]
        pos += 1
    return final
