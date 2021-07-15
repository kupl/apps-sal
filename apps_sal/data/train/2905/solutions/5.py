is_vowel = set("aeiou").__contains__

def nickname_generator(name):
    if len(name) < 4: return "Error: Name too short" # Take that Yu, Lee, Bob, and others!
    if is_vowel(name[2]): return name[:4]
    return name[:3]
