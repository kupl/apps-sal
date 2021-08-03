# cook your dish here
t = int(input())


def pattern(k):
    for i in range(1, k + 1):
        if i % 2 == 1:
            s = ''
            for j in range(i):
                s += chr(65 + j)
            s = ' ' * (26 - i) + s
            print(s)
        else:
            s = ''
            for j in range(1, i + 1):
                s += str(j)
            s = ' ' * (26 - i) + s
            print(s)


for _ in range(t):
    k = int(input())
    pattern(k)
