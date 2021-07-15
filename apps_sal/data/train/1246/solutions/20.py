for __ in range(int(input())):
    n=int(input())
    w=[int(x) for x in input().split()]
    j=[int(x) for x in input().split()]
    if (max(w) == max(j)):
        print("NO")
    else:
        print("YES")


