
def solve(ar):
    max = 0
    posn = -1
    for i in range(len(ar)):
        if ar[i]>max:
            max = ar[i]
            posn = i

    if posn == 0 or posn == len(ar)-1:
        return 1


    return 1+min(solve(ar[:posn]),solve(ar[posn+1:]))










t = int(input())

for i in range(t):
    n = int(input())
    h = list(map(int,input().split()))
    z = solve(h)
    print(z)







