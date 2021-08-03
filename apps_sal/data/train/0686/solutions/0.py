n = int(input())
l = []
for i in range(0, n):
    a, b, c = map(int, input().split())
    n1 = (2**0.5) * (a / b)
    n2 = 2 * (a / c)
    if n1 > n2:
        l.append("Elevator")
    else:
        l.append("Stairs")
for i in l:
    print(i)
