import math
test = int(input())
for i in range(test):
    p1, q1, p2, q2 = map(int, input().split())
    if math.sqrt(pow(p1, 2) + pow(q1, 2)) > math.sqrt(pow(p2, 2) + pow(q2, 2)):
        print("B IS CLOSER")
    else:
        print("A IS CLOSER")
