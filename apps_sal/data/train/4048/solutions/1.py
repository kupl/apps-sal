def pig_latin(word):
    return word if len(word) < 4 else word[1:]+word[0]+"ay"
