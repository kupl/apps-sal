t = int(input())

for _ in range(t):
    s, sg, fg, d, t = map(int, input().split(" "))

    car_speed = s + (d * 50 * 3.6) / t
    sebi = abs(car_speed - sg)
    fat = abs(car_speed - fg)
    if sebi < fat:
        print("SEBI")
    elif fat == sebi:
        print("DRAW")
    else:
        print("FATHER")
