def reverse_words(str):

    def reverser(word):
        if word == '':
            return word
        else:
            return reverser(word[1:]) + word[0]
    words_list = [reverser(x) for x in str.split(' ')]
    return ' '.join(words_list)
