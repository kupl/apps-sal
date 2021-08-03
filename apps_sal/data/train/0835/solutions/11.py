t = eval(input())
while t > 0:
    t -= 1
    r, c = list(map(int, input().split()))
    if ((r == 1 and c == 2) or (c == 1 and r == 2)):
        print("Yes")
    elif (r > 1 and c > 1 and (r % 2 == 0 or c % 2 == 0)):
        print("Yes")
    else:
        print("No")
