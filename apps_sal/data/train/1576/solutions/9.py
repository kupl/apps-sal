try:
    t = int(input())
    for a in range(t):
        k = int(input())
        lst = []
        for i in range(1, k + 1):
            lst.append(str(i))
        print("".join(lst))
        for i in range(k - 1):
            lst.append(lst[0])
            lst.pop(0)
            print("".join(lst))
except EOFError:
    pass
