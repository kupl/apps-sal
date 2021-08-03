t = eval(input())
for i in range(0, t):
    n = eval(input())
    directions = []
    for j in range(0, n):
        x = input()
        directions.append(x)
    for j in range(n - 1, -1, -1):
        output = ""
        if j == (n - 1):
            output = "Begin "
        else:
            if(directions[j + 1].find("Left") == -1):
                output = "Left "
            else:
                output = "Right "
        output = output + directions[j][directions[j].find("on"):]
        print(output)
