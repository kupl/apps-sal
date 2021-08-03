def is_palindrome(string):
    string = str(string)
    result = False
    i = 0

    for i in range(0, len(string) // 2):
        if string[i] == string[len(string) - i - 1]:
            result = True
            i += 1
        else:
            result = False
            break

    return result
