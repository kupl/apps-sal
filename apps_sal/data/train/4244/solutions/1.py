def palindrome(num):
    s = str(num)
    return "Not valid" if not isinstance(num, int) or num < 0 \
        else num > 10 and sum(s.count(d) % 2 > 0 for d in set(s)) < 2
