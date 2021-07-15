from collections import Counter

def longest_palindrome(s):
    c = Counter(filter(str.isalnum, s.lower()))
    return sum(v//2*2 for v in c.values()) + any(v%2 for v in c.values())
