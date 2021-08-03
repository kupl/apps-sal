import string


def find_char_index(word, mode='f'):
    word = [x for x in word]
    if mode == 'f':
        for index, char in enumerate(word):
            if char in string.punctuation:
                continue
            else:
                return index
    else:
        word.reverse()
        for index, char in enumerate(word):
            if char in string.punctuation:
                continue
            else:
                return len(word) - (index + 1)


def scramble_words(sentence):
    words = sentence.split(' ')
    final = []
    for word in words:

        first_index = find_char_index(word, 'f')
        last_index = find_char_index(word, 'l')

        res = ""
        ext_char = []
        for index, char in enumerate(word):
            if (char in string.punctuation) or (index == first_index) or (index == last_index):
                res += char
            else:
                res += "{}"
                ext_char.append(char)
        final.append(res.format(*sorted(ext_char)))

    return " ".join(final)
