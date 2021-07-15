def scramble(s1, s2):
    if None in (s1, s2):
        return False
    
    passed = []   #Added to avoid wasting time on suitable letters
    for letter in s2:
        if letter in passed: continue
        if (letter not in s1) or (s2.count(letter) > s1.count(letter)): return False #2nd condition VERY IMP, cause this was not at all obvious (guess I missed it completely), i.e.,must consider number of letters in s2 and s1
        passed.append(letter)
    else: return True
