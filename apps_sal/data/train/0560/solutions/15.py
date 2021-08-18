t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    a.remove(max(a))
    b.remove(max(b))
    if(sum(a) > sum(b)):
        print("Bob")
    elif sum(a) == sum(b):
        print("Draw")
    else:
        print("Alice")
