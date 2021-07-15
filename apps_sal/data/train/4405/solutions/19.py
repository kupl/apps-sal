def is_palindrome(string):
    start = 0
    end = -1
    palindrome = True
    for x in range(len(str(string))):
        if str(string)[start] == str(string)[end]:
            start += 1
            end -= 1
        else: palindrome = False
    return True if palindrome is True else False
