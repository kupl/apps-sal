x = int(input())
for i in range(x):
    (a, b) = map(int, input().split(' '))
    if(a > b):
        print(">")
    if(a < b):
        print("<")
    if(a == b):
        print("=")
