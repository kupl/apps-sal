for _ in range(int(input())):
    a = input()
    count = 0
    for i in a:
        if(i != "a"):
            count += 1
    print(2**len(a) - 2**count)
