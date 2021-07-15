def candies(s):
    if len(s)<2:
        return -1
    a=max(s)
    b=0
    for i in s:
        b=b+(a-i)
    return b

