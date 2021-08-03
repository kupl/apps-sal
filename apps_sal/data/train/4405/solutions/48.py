def is_palindrome(string):
    string = f"{string}"
    try:
        return string == "".join(reversed(string))
    except:
        return string == int("".join(reversed(string)))
