def permute_a_palindrome(input):
    return sum((input.count(c) % 2 for c in set(input))) < 2
