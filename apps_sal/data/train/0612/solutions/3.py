for _ in range(int(input())):
    bstr = input()
    opval = "Bad"
    for i in range(len(bstr) - 2):
        if bstr[i] == bstr[i + 2] and bstr[i] != bstr[i + 1]:
            opval = "Good"
            break
    print(opval)
