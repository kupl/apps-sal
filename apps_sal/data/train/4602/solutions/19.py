def is_anagram(test, original):
    a = list(test.lower())
    s = list(original.lower())
    if len(a) != len(s):
        return False
    else:
        for i in a:
            cond = False
            k = 0
            while k != len(s) and cond == False:
                if i == s[k]:
                    a.remove(i)
                    s.remove(i)
                    cond = True
                k += 1
            if cond == False:
                return False
        if len(a) != len(s):
            return False
        else:
            return True
