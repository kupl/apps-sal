def repeat_sequence_len(n):
    a = [n]
    while a.count(a[-1]) == 1:
        a.append(sum((int(c) ** 2 for c in str(a[-1]))))
    return len(a) - a.index(a[-1]) - 1
