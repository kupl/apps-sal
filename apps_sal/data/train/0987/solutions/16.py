# cook your dish here
import math
for i in range(int(input())):
    s, d, a, b = map(float, input().split())
    # For Tiger
    distance = s + d
    tiger = math.sqrt(2 * distance / a)
    # For Usain Bolt
    bolt = (s / b)
    if tiger <= bolt:
        print("Tiger")
    else:
        print("Bolt")
