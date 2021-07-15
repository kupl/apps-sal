def is_palindrome(s):
    length_array = len(s) - 1

    for i in range(len(s) // 2):
        if s[i].lower() != s[length_array - i].lower():
            return False
    return True

