def scramble(s1, s2):
    s1_count = dict.fromkeys(set(s1), 0)
    for i in s1:
        s1_count[i] += 1
    try:
        for i in s2:
            s1_count[i] -= 1
    except:
        return False
    return all((i >= 0 for i in s1_count.values()))
