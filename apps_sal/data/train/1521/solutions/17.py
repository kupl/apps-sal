# cook your dish here
try:
    t = int(input())
except:
    return
for q in range(t):
    n = int(input())
    ans = [0] * n
    l = []
    for w in range(n):
        lu = list(map(int , input().split()))
        l.append(lu)
    for i in range(n):
        x = l[i]
        for j in range(i+1,n):
            y = l[j]
            if x[0] < y[0] and x[1] > y[1]:
                ans[i] = ans[i] + 2
            elif y[0] < x[0] and y[1] > x[1]:
                ans[j] = ans[j] + 2
            else:
                ans[i] = ans[i] + 1 
                ans[j] = ans[j] + 1 
    s = ''.join((str(e) + " ") for e in ans)
    print(s)

