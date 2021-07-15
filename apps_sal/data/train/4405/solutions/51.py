def is_palindrome(input):
    
    if type(input) is int:
        return input == int(''.join([i for i in str(input)[::-1]]))
    else:
        return input == ''.join([i for i in input[::-1]])
