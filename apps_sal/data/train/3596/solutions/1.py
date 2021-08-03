def membership(amount, platinum, gold, silver, bronze):
    s1, s = dir(), locals()
    if s[s1[0]] >= s[s1[3]]:
        return s1[3].capitalize()
    if s[s1[0]] >= s[s1[2]]:
        return s1[2].capitalize()
    if s[s1[0]] >= s[s1[4]]:
        return s1[4].capitalize()
    if s[s1[0]] >= s[s1[1]]:
        return s1[1].capitalize()
    return "Not a member"
