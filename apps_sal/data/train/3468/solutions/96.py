from collections import Counter
def scramble(s1, s2):
    s1_count, s2_count = Counter(s1), Counter(s2)
    return all(s1_count[letter] >= s2_count[letter] for letter in s2) 
