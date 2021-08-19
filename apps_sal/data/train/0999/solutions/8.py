# cook your dish here

t = int(input())

while t:
    n = int(input())

    for i in range(1, n + 1):
        k = 1
        m = 65
        for j in range(n, 0, -1):
            if j > i:
                print(" ", end='')
            else:
                if i % 2 == 0:
                    print(k, end='')
                    k += 1
                else:
                    print(chr(m), end='')
                    m += 1

        print("")

    t -= 1
