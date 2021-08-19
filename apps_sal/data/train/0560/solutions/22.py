# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    a[len(a) - 1] = 0
    b[len(b) - 1] = 0
    if(sum(a) > sum(b)):
        print("Bob")
    elif(sum(b) > sum(a)):
        print("Alice")
    else:
        print("Draw")
