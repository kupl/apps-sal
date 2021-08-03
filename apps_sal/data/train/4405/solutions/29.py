def is_palindrome(string):
    x = len(str(string)) // 2
    if str(string)[:x] == str(string)[-1:-(x + 1):-1]:
        return True
    else:
        return False
