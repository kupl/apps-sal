for i in range(int(input())):
    x = input()
    a = x.split()[0]
    b = x.split()[1]
    print(str(int(str(int(a[::-1]) + int(b[::-1]))[::-1])))
