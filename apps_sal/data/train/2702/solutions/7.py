def create_anagram(s, t):
    s = list(s)
    for letter in t:
        if letter in s:
            s.remove(letter)
    return len(s)
