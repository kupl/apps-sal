def scramble(s1, s2):
    seen = []
    for letter in s2:
        if letter not in s1:
            return False
    for letter in s2:
        if letter in seen: continue
        if s1.count(letter) < s2.count(letter):
            return False
        else: seen.append(letter)
    return True
