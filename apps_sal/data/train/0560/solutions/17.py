a = int(input())
while a:
    a = a - 1
    b = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    h = sum(x) - max(x)
    g = sum(y) - max(y)
    if h < g:
        print("Alice")
    elif g < h:
        print("Bob")
    else:
        print("Draw")
