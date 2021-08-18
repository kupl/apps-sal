t = int(input())
for i in range(t):
    print("Case {}:".format(i + 1), end=" ")
    m, n = map(int, input().split())
    x, y = map(int, input().split())
    l = int(input())
    a = input()
    destx = a.count("R") - a.count("L")
    desty = a.count("U") - a.count("D")

    if (destx < 0 or destx > m) or (desty < 0 or desty > n):
        result = "DANGER"
    elif destx == x and desty == y:
        result = "REACHED"
    else:
        result = "SOMEWHERE"

    print(result)
