for o in range(int(input())):
    l = list(map(int, input().split()))
    s = sum(l) - l[-1]
    if(s * l[-1] <= 120):
        print("No")
    else:
        print("Yes")
