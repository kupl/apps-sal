def is_palindrome(s):
    iterations = len(s) // 2
    palindrome = True
    for i in range(iterations-1):
        a = s[i].lower()
        b = s[-(i + 1)].lower()
        if a != b:
            palindrome = False
            break    
    return palindrome

