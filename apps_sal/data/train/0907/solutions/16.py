for _ in range(int(input())):
    n = int(input())
    a = input()
    b = []
    c = 0
    for i in a:
        if i == "H" or i == "T":
            b.append(i)
    while len(b) > 2 * c:
        if len(b) % 2 != 0:
            print("Invalid")
            break
        elif b[2 * c] == "H" and b[2 * c + 1] == "T":
            c = c + 1
        else:
            print("Invalid")
            break
    if 2 * c == len(b):
        print("Valid")
