def triple_trouble(one, two, three):
    ans = ''
    for i in range(len(one)):
        ans+=one[i]
        ans+=two[i]
        ans+=three[i]
    return ans
