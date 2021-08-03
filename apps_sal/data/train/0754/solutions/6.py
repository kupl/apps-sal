for _ in range(int(input())):
    s = input()
    x = '02468'
    for i in x:
        if i in s:
            print(1)
            break
    else:
        print(0)
