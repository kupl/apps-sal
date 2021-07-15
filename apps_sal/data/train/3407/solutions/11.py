from functools import lru_cache

@lru_cache(maxsize=None)
def palindrome_chain_length(n):
    s1 = str(n)
    s2 = s1[::-1]
    return s1 != s2 and 1 + palindrome_chain_length(n + int(s2))
