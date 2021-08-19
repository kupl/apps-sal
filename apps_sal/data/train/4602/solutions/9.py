def is_anagram(test, original):
    go = len(test) == len(original)
    arr = []
    if go:
        for i in test:
            arr.append(i.lower() in original.lower())
        return False not in arr
    else:
        return False
