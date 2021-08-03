def string_clean(s):
    ans = ""
    for i in s:
        if not i.isdigit():
            ans += i

    return ans
