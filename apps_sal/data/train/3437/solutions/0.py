def decipher_word(word):
    i = sum(map(str.isdigit, word))
    decoded = chr(int(word[:i]))
    if len(word) > i + 1:
        decoded += word[-1]
    if len(word) > i:
        decoded += word[i+1:-1] + word[i:i+1]
    return decoded

def decipher_this(string):
    return ' '.join(map(decipher_word, string.split()))
