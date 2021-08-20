from itertools import count, islice


def palindrome(num, s):
    if isinstance(num, int) and isinstance(s, int) and (num > 0 <= s):
        palindromes = (x for x in count(max(num, 11)) if str(x) == str(x)[::-1])
        return list(islice(palindromes, s))
    return 'Not valid'
