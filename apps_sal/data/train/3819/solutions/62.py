def smash(words):
    newWord = ""
    for i in range(len(words)):
        if words[i] == words[-1]:
            newWord += words[i]
        else:
            newWord += words[i]
            newWord += " "
    return newWord
        

