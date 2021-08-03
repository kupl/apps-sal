def string_transformer(s):
    # 1st step: split the string (done)
    x = []
    s = s.split(" ")
    for i in range(1, 2 * len(s) - 1, 2):
        s.insert(i, " ")
    print(s)
    if "" in s:
        for i in s:
            i.replace("", " ")
    print(s)
    # 2nd step: reverse s (google to find the way)
    s.reverse()
    print(s)
    # 3rd step: reverse the case for each string in the list (google to find the way)
    for i in s:
        for j in i:
            if j == " ":
                x.append(j)
            elif j.isupper():
                j = j.lower()
                x.append(j)
            else:
                j = j.upper()
                x.append(j)
    print(x)
    # 4th step: join the list to make string
    return ''.join(x)
