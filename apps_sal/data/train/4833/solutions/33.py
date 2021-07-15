def replace_exclamation(s):
    vowels = "aeiouAEIOU"
    new = ""
    for char in s:
        if char in vowels:
            new += "!"
        else:
            new += char
            
    return new
