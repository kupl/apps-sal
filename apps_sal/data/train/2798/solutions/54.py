def to_alternating_case(string):
    ans = ''
    for i in string:
        if i == i.lower():
            ans += i.upper()
        else:
            ans += i.lower()
    return ans
