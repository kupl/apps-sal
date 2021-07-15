def triple_trouble(one, two, three):
    ans = ''
    for x in range(len(one)):
        ans += one[x] + two[x] + three[x]
    return ans
