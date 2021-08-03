for i in range(int(input())):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    s = int(l[2])
    ni = input().split()
    num = [int(x.strip()) for x in ni]
    p = sorted(list(range(len(num))), key=num.__getitem__)
    for j in p:
        print(j + 1, end=' ')
    print()
