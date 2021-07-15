def is_palindrome(string):
    try: return str(string) == str(string)[::-1]
    except: return False
