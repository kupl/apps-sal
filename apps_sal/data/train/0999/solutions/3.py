# cook your dish here
for i in range(int(input())):
    n = int(input())
    count = 0
    for j in range(1, n + 1):
        c = 65
        z = 1
        space = n - j
        star = j
        if j % 2 != 0:
            print(space * ' ', end='')
            for l in range(star):
                print(chr(c), end='')
                c += 1

        else:
            print(space * ' ', end='')
            for l in range(star):
                print(z, end='')
                z = z + 1
        print()
