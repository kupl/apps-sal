def anagrams(word, words):
    lst = []
    for elem in words:
        if sorted(word) == sorted(elem):
            lst.append(elem)
    return lst
    #your code here

