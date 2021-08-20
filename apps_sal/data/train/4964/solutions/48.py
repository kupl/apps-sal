def is_uppercase(inp):
    ans = ''
    for x in inp:
        if x.isalpha() == True:
            ans = ans + x
    return ans.isupper()
