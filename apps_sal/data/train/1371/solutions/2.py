# cook your dish here
for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    c = 0
    for i in a:
        aa = i + k
        if aa % 7 == 0:
            c += 1
    print(c)
