def palindrome(num):
    def is_palindrome(chunk): return int(chunk) > 9 and chunk == chunk[::-1]
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    i = 0
    while(True):
        if is_palindrome(str(num + i)):
            return num + i
        if is_palindrome(str(num - i)):
            return num - i
        i += 1
