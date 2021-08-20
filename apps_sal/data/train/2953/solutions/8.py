def numericals(s):
    sdict = {}
    ans = ''
    for i in range(len(s)):
        sdict[s[i]] = 0
    for i in range(len(s)):
        sdict[s[i]] += 1
        ans += str(sdict[s[i]])
    return ans
