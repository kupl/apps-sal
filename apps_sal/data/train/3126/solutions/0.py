def palindrome_rearranging(s):
    return sum(s.count(c) % 2 for c in set(s)) < 2
