for _ in range(int(input())):
    H, M = [int(n) for n in input().split(":")]
    if (H >= 12):
        H -= 12
    if(M == 60):
        M = 0
        H += 1
    angleH = H * 30 + M * 0.5
    angleM = M * 6
    angle = abs(angleH - angleM)
    angle = min(360 - angle, angle)
    if not (angle > int(angle)):
        angle = int(angle)
    print(str(angle) + " degree")
