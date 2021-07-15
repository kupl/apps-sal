def palindrome(num):
    if type(num) != int or num < 0:
        return "Not valid"
    k = str(num)
    if k == k[::-1]:
        return True
    else:
        return False
