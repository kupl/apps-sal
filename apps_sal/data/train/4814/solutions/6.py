def is_palindrome(s):
    s = s.lower()
    _list = list(s)
    _list.reverse()
    str = ""
    for i in _list:
        str += i
    return str == s
