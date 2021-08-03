def solution(string, ending):
    e = list(ending)
    s = list(string)
    el = len(e)
    sl = len(s)
    if el == 0:
        return True
    elif el > sl:
        return False
    else:
        i = sl - el
        j = 0
        ans = True
        while i < sl:
            if e[j] != s[i]:
                ans = False
                break
            i = i + 1
            j = j + 1
        return ans
    pass
