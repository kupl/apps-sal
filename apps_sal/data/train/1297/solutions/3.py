n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    if x > y:
        print(">")
    elif x < y:
        print("<")
    elif x == y:
        print("=")
