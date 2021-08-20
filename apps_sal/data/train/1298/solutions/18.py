for i in range(0, int(input())):
    (n, m) = (int(input()), list(map(int, input().split())))
    print(sum([1 for i in m if i > m[0]]))
