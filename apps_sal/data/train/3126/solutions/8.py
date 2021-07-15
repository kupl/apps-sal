def palindrome_rearranging(s):
    return sum(s.count(char) % 2 for char in set(s)) <= 1

