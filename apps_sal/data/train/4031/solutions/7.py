def interpreter(s, tape):
    m, pointer, j = list(map(int, tape)), 0, 0
    find, find_ = [i for i, j in enumerate(s) if j == '['],[i for i, j in enumerate(s) if j == ']']
    opened, closed = {i: j for i, j in zip(find, find_[::-1])}, {i: j for i, j in zip(find_[::-1], find)} # open and closed braces
    while j < len(s) and 0<=pointer<len(m):
        if s[j] == "*" :             m[pointer] ^= 1
        elif s[j] == '>' :           pointer += 1
        elif s[j] == '<' :           pointer -= 1
        elif s[j] == "[":
            if m[pointer] == 0 :  j = opened[j]
        elif s[j] == ']':
            if m[pointer] == 1 :  j = closed[j]
        j += 1
    return "".join(map(str, m))
