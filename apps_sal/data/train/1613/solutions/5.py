def solution(string,markers):
    lst = string.split('\n')
    for i, s in enumerate(lst):
        for m in markers:
            f = s.find(m)
            s = s[0:f] if f >= 0 else s[:]
        lst[i] = s.strip()

    return '\n'.join(lst)

