from functools import lru_cache


@lru_cache(None)
def count_subsequences(needle, haystack):
    return sum(count_subsequences(needle[1:], haystack[i + 1:])
               for i, char in enumerate(haystack) if char == needle[0]) if needle else 1
