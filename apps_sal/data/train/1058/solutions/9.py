def fun():
    T = int(input())
    for i in range(T):
        x = input()
        st = str('')
        for j in x:
            n = str(int(j) - 2)
            st += n
        print(st)


fun()
