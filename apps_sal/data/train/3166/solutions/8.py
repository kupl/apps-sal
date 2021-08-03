def circle_slash(n):
    s = format(n, 'b')
    return int(s[1:] + s[0], 2)
