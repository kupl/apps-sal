def string_letter_count(s):
    s = s.lower()
    L1 = []
    for i in s:
        L1.append(i)
    L1.sort()
    s = "".join(L1)
    A = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
    L = []
    for i in s:
        if i not in L:
            if i in A:
                L.append(str(s.count(i)))
                L.append(str(i))
    return "".join(L)
