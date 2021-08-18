t = int(input())
for z in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if n % 2 == 1 and a[0] == 1:
        x = list(reversed(a))
        for i in range((len(a) - 1) // 2):
            if a[i] + 1 == x[i + 1]:
                c = 0
            else:
                c = 1
                break
        if c == 1:
            print("no")
        else:
            print("yes")
    else:
        print("no")
