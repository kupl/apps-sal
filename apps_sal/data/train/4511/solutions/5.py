def permute_a_palindrome(s):
    return sum((f % 2 for f in __import__('collections').Counter(s).values())) < 2
