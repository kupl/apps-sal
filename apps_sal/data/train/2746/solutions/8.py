def check_vowel(string, position):
    if position <0 or position >len(string): return False
    return string[position].lower() in "aeiou"
