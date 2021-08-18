def sortme(words):
    arr = []

    if len(words) > 1:
        for i in words:
            arr.append(i.lower())
        arr = sorted(arr)
        print(arr)

        m = []
        for i in arr:
            try:
                j = words.index(i)
                if i.islower():
                    m.append(i)
            except:
                m.append(i.capitalize())

        return m
    else:
        return words
