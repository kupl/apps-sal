def pig_latin(word):
    return word[1:]+word[0]+'ay' if len(word)>3 else word
