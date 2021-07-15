def absent_vowel(x): 
    return "aeiou".index((set("aeiou")-set(x)).pop())
