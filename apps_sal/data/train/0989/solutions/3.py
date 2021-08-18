for i in range(int(input())):
    x, y, k = map(int, input().split())
    if(((x + y) // k) % 2 == 0):
        print("Chef")
    else:
        print("Paja")
