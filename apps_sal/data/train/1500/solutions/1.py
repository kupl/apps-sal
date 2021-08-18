for _ in range(int(input())):
    b = 0
    mx = 0
    for i in input():
        if i == "(":
            b += 1
        else:
            b -= 1
        mx = max(b, mx)
    print("(" * mx + ")" * mx)
