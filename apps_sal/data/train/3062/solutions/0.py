def palindrome(num):
    if type(num) is not int or num < 1:
        return "Not valid"
    return num == int(str(num)[::-1])
