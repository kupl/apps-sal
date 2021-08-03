def replace_exclamation(s):
    l = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    s1 = ""
    for i in s:
        if(i in l):
            s1 = s1 + "!"
        else:
            s1 = s1 + i
    return s1
