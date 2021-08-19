# cook your dish here
for w in range(int(input())):
    danx, dany = list(map(int, input().split()))
    detx, dety = list(map(int, input().split()))
    u = int(input())
    l = input()
    x = y = 0
    for i in range(len(l)):
        if l[i] == "U":
            y += 1
        elif l[i] == "D":
            y -= 1
        elif l[i] == "L":
            x -= 1
        elif l[i] == "R":
            x += 1
    w += 1
    if detx == x and dety == y:
        print("Case"" " + str(w) + ":"" ""REACHED")
    elif x < 0 or y < 0 or x > danx or y > dany:
        print("Case"" " + str(w) + ":"" ""DANGER")
    else:
        print("Case"" " + str(w) + ":"" ""SOMEWHERE")
