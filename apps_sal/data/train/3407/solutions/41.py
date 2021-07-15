def is_palindrome(n):
    string = str(n)
    reverse = int(''.join(reversed(string)))
    if n == reverse:
        return True
    else:
        return False
    
def palindrome_chain_length(n):
    i = 0
    while True:
        if is_palindrome(n):
            break
        else: 
            n += int(''.join(reversed(str(n))))
        i += 1
    return i
