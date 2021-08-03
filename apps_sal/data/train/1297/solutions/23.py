t = int(input())
for k in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    if a < b:
        print("<")
    elif a > b:
        print(">")
    else:
        print("=")
