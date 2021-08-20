def repeat_str(repeat, string):
    (i, ans) = (0, '')
    while i < repeat:
        ans += string
        i = i + 1
    return ans
