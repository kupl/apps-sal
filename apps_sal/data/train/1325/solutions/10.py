for _ in range(int(input())):
    l = list(map(int, input().split()))
    a = l[0]
    b = l[1]
    c = l[2]
    d = l[3]
    A = d - b
    M = d - c
    O = d - a
    print(A, M, O)
