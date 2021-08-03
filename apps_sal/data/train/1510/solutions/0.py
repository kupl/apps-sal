for _ in range(int(input())):
    s = input()
    c = 0
    for i in s:
        if i.isalpha() and i.isupper():
            c += 1
    print(c)
