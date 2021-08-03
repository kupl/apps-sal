def who_is_paying(name):
    # your code here
    ans = list()
    sec = ''
    if len(name) <= 2:
        ans = [name]
    else:
        sec = name[0:2]
        ans = [name, sec]
    return ans
