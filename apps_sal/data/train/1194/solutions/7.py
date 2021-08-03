t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = list(input())
    print(n - (abs(s.count("L") - s.count("R")) + abs(s.count("U") - s.count("D"))))
