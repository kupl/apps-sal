t = int(input())
i = 0
while i < t:
    n = int(input())
    A = []
    A = input().split()
    m = int(input())
    B = []
    B = input().split()
    j = 0
    a = -1
    while j < m:
        c = 1
        if B[j] in A:
            b = A.index(B[j])
            A.remove(B[j])
            if b >= a:
                a = b
                c = 1
            else:
                c = 0
                break
        else:
            c = 0
            break
        j += 1
    if c == 1:
        print("Yes")
    else:
        print("No")
    i += 1
