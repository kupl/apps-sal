from collections import Counter


def permute_a_palindrome(s: str) -> bool:
    return len(s) % 2 == sum(i % 2 for i in list(Counter(s).values()))

