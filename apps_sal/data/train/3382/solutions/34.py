def lowercase_count(strng):
    ans = 0
    for x in strng:
        if x.islower() == True:
            ans += 1
    return ans
