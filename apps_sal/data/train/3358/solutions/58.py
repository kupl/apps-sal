def correct(string):
    print(string)
    a = ""
    bad = {"0": "O", "1": "I", "5": "S"}
    for i in string:
        # print(i)
        if i in bad:
            a = a + bad.get(i)
        else:
            a = a + i
    return a
