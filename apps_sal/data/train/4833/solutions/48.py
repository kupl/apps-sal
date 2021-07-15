def replace_exclamation(s):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for letter in s:
        if letter.lower() in vowels:
            result += "!"
        else:
            result += letter
    return result
