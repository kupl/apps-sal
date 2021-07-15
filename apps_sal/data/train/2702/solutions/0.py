from collections import Counter

def create_anagram(s, t):
    return sum((Counter(s) - Counter(t)).values())
