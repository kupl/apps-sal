for _ in range(int(input())):
    n = int(input())
    a = input().split()
    b = input().split()
    Sum = 0
    suma = 0
    sumb = 0
    for i in range(len(a)):
        if i == 0:
            suma += int(a[i])
            sumb += int(b[i])
            if suma == sumb:
                Sum += int(a[i])
        else:
            if suma == sumb:
                suma += int(a[i])
                sumb += int(b[i])
                if suma == sumb:
                    Sum += int(a[i])
            else:
                suma += int(a[i])
                sumb += int(b[i])
    print(Sum)
