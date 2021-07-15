def repeat_sequence_len(n):
    s = []

    while True:
        n = sum(int(i) ** 2 for i in str(n))
        if n not in s:
            s.append(n)
        else:
            return len(s[s.index(n):])
