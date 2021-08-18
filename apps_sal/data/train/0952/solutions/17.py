try:
    t = int(input())
    for _ in range(t):
        s = input()
        a = 'aeiou'
        ar = [1, 5, 9, 15, 21]
        c = 0
        for i in s:
            if i not in a:

                x = ord(i) - 96
                if x >= 18:
                    c += abs(x - 21)
                elif x >= 12:
                    c += abs(x - 15)
                elif x >= 7:
                    c += abs(x - 9)
                elif x >= 3:
                    c += abs(x - 5)
                else:
                    c += abs(x - 1)
        print(c)
except EOFError:
    pass
