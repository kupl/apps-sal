def palindrome(num):
    return "Not valid" if not isinstance(num, int) or num < 0 else 0 if num < 10 else len([c for i, c in enumerate(str(num)[:-1]) if str(num)[i+1] == c or len(str(num)) - i > 3 and str(num)[i+3] == c or len(str(num)) - i > 2 and str(num)[i+2] == c])
