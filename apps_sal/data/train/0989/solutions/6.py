for _ in range(int(input())):
    a = input().split()
    x = int(a[0])
    y = int(a[1])
    k = int(a[2])

    if ((x + y) // k) % 2:
        print("Paja")
    else:
        print("Chef")
