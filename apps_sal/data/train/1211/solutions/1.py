for i in range(int(input())):
    txt = input()
    while True:
        l = len(txt)
        x = txt.replace('abc', '')
        if len(x) == l:
            break
        txt = x
    print(x)
