def find_missing_number(sequence):
    a = []
    for i in sequence.split():
        if i.isdigit():
            a.append(int(i))
        else:
            return 1
    if a == []: return 0
    for i in range(1,max(a)+1):
        if not i in a:
            return i
    return 0
