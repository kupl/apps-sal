for _ in range(int(input())):
    z = list(map(int, input().split()))
    if z[0] == z[1]:
        print("=")
    elif z[0] > z[1]:
        print(">")
    else:
        print("<")
