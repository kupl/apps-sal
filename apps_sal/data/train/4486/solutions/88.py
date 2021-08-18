def repeat_it(s, n):
    if type(s) == str:
        x = 1
        st = ''
        while x <= n:
            st += s
            x += 1
        return st
    else:
        return "Not a string"
