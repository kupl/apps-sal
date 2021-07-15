
t = int(input())

for loop in range(t):

    n = int(input())
    p = list(map(int,input().split()))

    nf = float("inf")
    now = float("inf")

    ans = "Yes"
    for i in p:

        if i == now+1:
            now += 1
        elif i > nf:
            ans = "No"
            break
        else:
            nf = i
            now = i

    print (ans)

