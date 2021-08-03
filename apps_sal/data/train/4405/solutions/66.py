def is_palindrome(string):
    string = list(str(string))

    while len(string) > 1:
        if string[0] != string[-1]:
            return False

        string.pop(0)
        string.pop()

    return True
