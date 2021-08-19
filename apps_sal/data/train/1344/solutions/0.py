# cook your dish here
def __starting_point():
    try:
        for _ in range(int(input())):
            element = int(input())
            l = list(map(int, input().split()))
            a = min(l)
            l.remove(a)
            b = min(l)
            print(a + b)
    except EOFError:
        print('EOFError')


__starting_point()
