for w in range(int(input())):
    m, n = list(map(int, input().split()))
    rx, ry = list(map(int, input().split()))
    u = int(input())
    s = input()
    x = y = 0
    for i in range(len(s)):
        if s[i] == "U":
            y += 1
        elif s[i] == "D":
            y -= 1
        elif s[i] == "L":
            x -= 1
        elif s[i] == "R":
            x += 1
    w += 1
    if rx == x and ry == y:
        print("Case"" " + str(w) + ":"" ""REACHED")
    elif x < 0 or y < 0 or x > m or y > n:
        print("Case"" " + str(w) + ":"" ""DANGER")
    else:
        print("Case"" " + str(w) + ":"" ""SOMEWHERE")
