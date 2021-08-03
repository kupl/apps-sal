# cook your dish here
def __starting_point():
    try:
        while int(input()) != 0:
            l = list(map(int, input().split()))
            l1 = [0] * len(l)
            for i in range(len(l)):
                l1[l[i] - 1] = i + 1
            print("ambiguous" if l == l1 else "not ambiguous")
    except EOFError:
        print('EOFError')


__starting_point()
