def is_palindrome(string):
    if type(string) == type(1):
        string = str(string)
    m = len(string)//2
    if len(string) % 2 != 0:
        l,r = string[:m],string[m+1:]
    else:
        l,r = string[:m],string[m:]
    return True if l == r[::-1] else False
