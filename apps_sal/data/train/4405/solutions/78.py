def is_palindrome(string):
    # print(string)
    string = str(string)
    return string == string[::-1]
