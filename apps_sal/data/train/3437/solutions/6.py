import re


def decipher_this(string):
    # list to save decrypted words
    decrypted = []
    for word in string.split():
        # get number in string
        re_ord = re.match(r'\d+', word).group()
        # replace number by ascii letter and transform word in a list
        new_word = list(re.sub(re_ord, chr(int(re_ord)), word))
        # swap second and last letter in the word list
        if len(new_word) > 2:
            new_word[1], new_word[-1] = new_word[-1], new_word[1]
        # save the word in the string list
        decrypted.append(''.join(new_word))
    # return the decrypted words list as a string
    return ' '.join(decrypted)
