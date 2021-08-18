a = int(input())
while (a != 0):
    S, x, y, z = input().split(" ")
    x = int(x)
    y = int(y)
    z = int(z)
    S = int(S)
    count = 0
    if x + y + z <= S:
        count = 1
    elif (x + y <= S and z <= S) or (y + z <= S and x <= S):
        count = 2

    else:
        count = 3
    print(count)
    a -= 1
