def is_palindrome(string):
    string = str(string)
    for i in range(0, len(string) // 2):
        if string[i] == string[-i - 1]:
            pass
        else:
            return False
    return True
