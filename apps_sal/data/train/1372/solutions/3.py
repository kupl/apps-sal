# cook your dish here
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    d1 = (x1**2 + y1**2)**0.5
    d2 = (x2**2 + y2**2)**0.5
    if(d1 > d2):
        print("B IS CLOSER")
    else:
        print("A IS CLOSER")
