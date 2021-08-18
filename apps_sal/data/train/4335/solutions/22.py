def anagrams(word, words):
    list = []
    word = sorted(word)
    for i in range(len(words)):
        if word == sorted(words[i]):
            list.append(words[i])
        else:
            pass
    return(list)
