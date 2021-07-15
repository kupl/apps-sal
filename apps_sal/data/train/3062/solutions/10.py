def palindrome(num):
    if type(num) != int or num < 0:
        return "Not valid"
    else:
        return int(str(num)[::-1]) == num
