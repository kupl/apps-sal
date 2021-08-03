for _ in range(int(input())):
    str = input()
    c = 0
    for i in range(len(str)):
        if((str[i] >= 'A' and str[i] <= 'J')):
            c += 1
    print(c)
