def f(a, b):
    if(len(b) == 0):
        return True
    if(a[0] > b[0]):
        return False
    return f(b, a[1:])


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    if(f(a, b) == True or f(b, a) == True):
        print("YES")
    else:
        print("NO")
