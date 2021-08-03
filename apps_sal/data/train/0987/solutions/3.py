for i in range(int(input())):
    finish, distanetobolt, tigerAcceleration, boltspeed = map(int, input().split())
    t1 = ((2 * (finish + distanetobolt) / (tigerAcceleration))**0.5)
    t2 = (finish / boltspeed)
    if t1 > t2:
        print("Bolt")
    elif t1 < t2:
        print("Tiger")
    else:
        print("Tiger")
