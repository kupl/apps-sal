T = int(eval(input("")))
for i in range(T):
    n, v1, v2 = list(map(int, input("").split(" ")))
    t1 = 2**0.5 * n / v1
    t2 = 2 * n / v2
    if t1 > t2:
        print("Elevator")
    else:
        print("Stairs")
