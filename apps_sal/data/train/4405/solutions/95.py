def is_palindrome(string):
    string = str(string)
    for i in range(len(string) // 2):
        if len(string) % 2 == 0:
            if string[len(string) // 2 - i - 1] != string[i + len(string) // 2]:
                return False
        elif len(string) % 2 == 1:
            if string[len(string) // 2 - i - 1] != string[i + len(string) // 2 + 1]:
                return False
    return True
