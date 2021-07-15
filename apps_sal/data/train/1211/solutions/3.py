for t in range(int(input())) :
    x = input()
    while 'abc' in x :
        x = x.replace('abc','')
    print(x)
