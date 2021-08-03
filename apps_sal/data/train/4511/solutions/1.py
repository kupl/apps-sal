def permute_a_palindrome(txt):
    return len([txt.count(c) for c in txt if txt.count(c) % 2]) < 2
