def stringy(size):
    ans = ''
    for place in range(size):
        if place % 2 == 0:
            ans += '1'
        else:
            ans += '0'
    return ans
