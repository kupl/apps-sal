t = int(input())
for k in range(t):
    n = int(input())
    a = input().split()
    b = input().split()
    for j in range(n):
        a[j] = int(a[j])
        b[j] = int(b[j])
    a.remove(max(a))
    b.remove(max(b))
    s1 = sum(a)
    s2 = sum(b)
    if (s1 > s2):
        print("Bob")
    elif (s2 > s1):
        print("Alice")
    else:
        print("Draw")
