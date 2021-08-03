import math
n = int(input())
for _ in range(2 * n):
    try:
        a, b, c, d = list(map(int, input().split()))
        if math.sqrt((a**2) + (b**2)) > math.sqrt((c**2) + (d**2)):
            print("B IS CLOSER")
        else:
            print("A IS CLOSER")
    except:
        print()
