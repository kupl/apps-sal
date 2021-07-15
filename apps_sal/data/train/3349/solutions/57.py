def find_missing_number(s):
    if s == "":    return 0
    l = s.split(" ")
    for i in l:
        if not i.isdigit():
            return 1
    l = sorted([int(i) for i in l])
    for i in range(len(l)):
        if i + 1 != l[i]:
            return i + 1
    return 0
