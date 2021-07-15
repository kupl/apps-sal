def grabscrab(word, possible_words):
    result = []
    for possible_word in possible_words:
        if len(possible_word) == len(word):
            if False not in [c in word for c in possible_word] and [False for c in possible_word if possible_word.count(c) == word.count(c)]:
               result.append(possible_word)
    return result
