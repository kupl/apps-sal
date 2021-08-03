def anagrams(word, words):
    ans = []
    or1 = 0
    or2 = 0
    for i in word:
        or1 += ord(i)
    for i in words:
        or2 = 0
        for x in i:
            or2 += ord(x)
        if or1 == or2:
            ans += [i]
    return ans
