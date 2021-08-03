t = int(input())
for I in range(t):
    a, b, n = [int(i) for i in input().split()]
    if(n % 3 == 0):
        print(a)
    elif(n % 3 == 1):
        print(b)
    else:
        print(a ^ b)
