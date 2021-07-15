def is_palindrome(string):
    result = str(string)
    reversed_string = ''.join(reversed(result))
    if result.lower() == reversed_string.lower():
        return True
    else:
        return False
