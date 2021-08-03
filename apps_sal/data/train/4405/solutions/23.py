def is_palindrome(input):
    str_input = str(input)

    for i in range(len(str_input) // 2 - 1):
        if str_input[i] != str_input[-(i + 1)]:
            return False

    return True
