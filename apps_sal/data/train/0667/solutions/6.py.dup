# cook your dish here
try:
    for _ in range(int(input())):
        n, d = [int(i) for i in input().split()]
        a = [int(i) for i in input().split()]
        i = n - 1
        r = d
        while i >= 0:
            r = (r // a[i]) * a[i]
            i -= 1
        print(r)
except EOFError as error:
    pass
