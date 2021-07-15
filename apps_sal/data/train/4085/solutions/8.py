from random import shuffle

def mix_words(s):
    if type(s) != str:
        return "undefined"
    else:
        splitter = s.split(' ')
        for i, word in enumerate(splitter):
            punctuation = not word[-1].isalpha()
            if len(word) > 3 + punctuation:
                middle = list(word[1:-1 - punctuation])
                while middle == list(word[1:-1 - punctuation]):
                    shuffle(middle)
                splitter[i] = word[0] + ''.join(middle) + word[-1  - punctuation:]
        return ' '.join(splitter)
