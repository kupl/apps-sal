def is_palindrome(string):
    string = str(string)
    output = True
    for i in range(0, len(string) // 2):
        print(i)
        if string[i] != string[len(string) - i - 1]:
            output = False
            return output
    return output
