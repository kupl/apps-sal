import re


def decipher_this(string):
    decrypted = []
    for word in string.split():
        re_ord = re.match('\\d+', word).group()
        new_word = list(re.sub(re_ord, chr(int(re_ord)), word))
        if len(new_word) > 2:
            (new_word[1], new_word[-1]) = (new_word[-1], new_word[1])
        decrypted.append(''.join(new_word))
    return ' '.join(decrypted)
