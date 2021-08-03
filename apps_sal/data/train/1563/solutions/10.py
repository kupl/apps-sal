# /usr/bin/python

def main():
    test = int(input())
    for i in range(test):
        x = input()
        l = x.split()
        a = str(l[0])
        b = str(l[1])
        a = a[::-1]
        b = b[::-1]
        c = int(a) + int(b)
        s = str(c)
        s = s[::-1]
        print(int(s))


def __starting_point():
    main()


__starting_point()
