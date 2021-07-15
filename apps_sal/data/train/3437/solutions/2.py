def decipher_this(string):
    words = []
    for word in string.split():
        code = ''.join(char for char in word if char.isdigit())
        new_word = chr(int(code))+''.join(char for char in word if not char.isdigit())
        words.append(new_word[:1]+new_word[-1]+new_word[2:-1]+new_word[1] if len(new_word)>2 else new_word)
    return ' '.join(words)
