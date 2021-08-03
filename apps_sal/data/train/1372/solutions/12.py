for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    A = (x1**2 + y1**2)**(1 / 2)
    B = (x2**2 + y2**2)**(1 / 2)
    if A < B:
        print("A IS CLOSER")
    else:
        print("B IS CLOSER")
