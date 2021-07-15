def absent_vowel(x): 
    code = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
    for i in code:
        if i not in x:
            return code[i] 

