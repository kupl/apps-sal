from math import sqrt
for t in range(int(input())):
    ax, ay, bx, by = map(int, input().split())
    adist = sqrt(ax**2 + ay**2)
    bdist = sqrt(bx**2 + by**2)
    if adist > bdist:
        print("B IS CLOSER")
    else:
        print("A IS CLOSER")
