n = int(input())
for i in range(n):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    if a >= b:
        print("Yes")
    else:
        print("No")
