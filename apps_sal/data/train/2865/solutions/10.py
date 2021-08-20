def solution(string):
    s = list(string)
    j = len(s) - 1
    for i in range(len(s)):
        if i < j:
            (s[i], s[j]) = (s[j], s[i])
            j = j - 1
        else:
            continue
    s1 = ''.join(s)
    return s1
