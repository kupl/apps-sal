for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    (mini, maxi) = (l[0] * l[1], l[-1] * l[-2])
    print(maxi, mini)
