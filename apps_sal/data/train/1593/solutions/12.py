# cook your dish here
a = [100, 50, 10, 5, 2, 1]
for i in range(int(input())):
    n = int(input())
    c = 0
    for i in a:
        if n != 0:
            if n // i != 0:
                c += n // i
                n -= ((n // i) * i)
        else:
            break
    print(c)
