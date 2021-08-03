def is_palindrome(string):
    string = str(string)
    string_length = len(string)
    for i in range(string_length // 2):
        if string[i] != string[string_length - 1 - i]:
            return False
    return True
