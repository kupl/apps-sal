T = int(input())
for t in range(T):
    a, b, n = [int(i) for i in input().split()]
    if n%3 == 2:
        print(a^b)
    elif n%3 == 1:
        print(b)
    else:
        print(a)

