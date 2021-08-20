def name_in_str(s, name):
    s = s.lower()
    name = name.lower()
    result = False
    x = 0
    helper = []
    for i in range(len(name)):
        for j in range(x, len(s)):
            if name[i] == s[j]:
                x = j + 1
                helper.append(name[i])
                break
    if list(name) == helper:
        result = True
    return result
