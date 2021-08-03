# cook your dish here
for _ in range(int(input())):
    x, y, k = map(int, input().split())
    a = (x + y) // k
    if a % 2 == 0:
        print("Chef")
    else:
        print("Paja")
