def is_palindrome(string):
    return all([str(string)[i] == str(string)[len(str(string)) - i - 1] for i in range(int(len(str(string))/2))])
