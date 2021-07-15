def palindrome(n):
    if type(n) != int or n < 0:
        return "Not valid"
    s = str(n)
    return n > 10 and sum(s.count(d) % 2 for d in set(s)) < 2
