def is_anagram(s, l):
    n = len(s)
    if len(l) != n:
        return False
    s = s.lower()
    l = l.lower()
    h = [0 for x in range(26)]
    for i in range(n):
        h[ord(s[i]) - 97] += 1
        h[ord(l[i]) - 97] -= 1
    return h.count(0) == 26
