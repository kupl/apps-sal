n = int(input())
l = [int(i) for i in input().split()]
q = int(input())
while q != 0:
    a = int(input())
    x = l.pop(a - 1)
    print(x)
    q = q - 1
