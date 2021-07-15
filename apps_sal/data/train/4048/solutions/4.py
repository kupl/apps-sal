def pig_latin(word):
    return word if len(word) < 4 else f"{word[1:]}{word[:1]}ay" 
