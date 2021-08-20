def anagrams(word, words):
    letter = {x: word.count(x) for x in word}
    result = []
    for i in words:
        letters = {x: i.count(x) for x in i}
        if letters == letter:
            result.append(i)
    return result
