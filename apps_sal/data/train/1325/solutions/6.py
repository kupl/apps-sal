t = int(input())
for i in range(t):
    o = list(map(int, input().split()))
    A = int(o[0])
    B = int(o[1])
    C = int(o[2])
    D = int(o[3])
    orange = D - A
    apple = D - B
    mango = D - C
    print(apple, mango, orange, end=' ')
    print()
