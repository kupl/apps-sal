def is_palindrome(string):
    if type(string) is int:
        st_res = str(string)
        if st_res == st_res[::-1]:
            return True
        else:
            return False
    if type(string) is str:
        if string == string[::-1]:
            return True
        else:
            return False
