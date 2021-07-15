def palindrome(n):
    try:
        return 1. * n == int(str(n)[::-1])
    except:
        return "Not valid"
