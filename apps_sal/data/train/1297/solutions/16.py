t = int(input())
for i in range(t):
    (a, b) = list(map(int, input().split(" ")))
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")
