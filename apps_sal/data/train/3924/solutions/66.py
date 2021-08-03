def reverse_words(text):
    words = text.split(' ')
    backwards = []
    for word in words:
        backword = ''
        for c in range(len(word) - 1, -1, -1):
            backword += word[c]
        backwards.append(backword)
    return ' '.join(backwards)
