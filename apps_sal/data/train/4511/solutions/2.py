def permute_a_palindrome(stg):
    return sum((stg.count(c) % 2 for c in set(stg))) == len(stg) % 2
