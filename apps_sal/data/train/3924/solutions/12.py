def reverse_words(text):
    l = text.split(' ')
    for i in range(len(l)):
        l[i] = l[i][::-1]
    return ' '.join(l)
