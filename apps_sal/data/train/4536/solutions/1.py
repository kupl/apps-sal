def capitals_first(string):
    words = string.split()
    st1 = []
    st2 = []
    for word in words:
        if word[0].isalpha():
            if word[0].isupper():
                st1.append(word)
            else:
                st2.append(word)
    return ' '.join(st1 + st2)
