def odd_one_out(s):
    from collections import Counter
    c = Counter(s)
    ans = []
    for i in s[::-1]:
        try:
            if c[i] % 2 == 1:
                ans.append(i)
                del c[i]
        except:
            pass
                
    return ans[::-1]
