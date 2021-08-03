def is_palindrome(string):
    return "".join("{}".format(string)[::-1]) == "{}".format(string)
