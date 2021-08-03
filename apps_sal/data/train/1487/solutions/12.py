for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    x = int(input())

    A, B = 0, 0
    i, j = 0, n - 1

    while i < j:
        B += 1
        chocsA = x * lst[j]

        while i < j and chocsA >= lst[i]:
            chocsA -= lst[i]
            i += 1
            A += 1

        lst[i] -= chocsA
        j -= 1

    if i == j:
        if chocsA > 0:
            A += 1

        else:
            if A >= B:
                A += 1
            else:
                B += 1

    print(A, B)
