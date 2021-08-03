def clean_string(s):

    ans = ""
    for letter in s:
        if letter == "#":
            if len(ans) > 0:
                ans = ans[:-1]
        else:
            ans += letter

    return ans
