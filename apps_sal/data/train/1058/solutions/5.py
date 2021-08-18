for t in range(int(input())):
    n = input()
    num = ""
    for c in n:
        num += str(int(c) - 2)

    print(num)
