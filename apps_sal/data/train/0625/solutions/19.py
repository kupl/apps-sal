
# code from gfg: https://www.geeksforgeeks.org/count-sub-arrays-sum-divisible-k/
while(1):
    for _ in range(int(input())):
        n=int(input())
        l=list(map(int,input().split()))
        g=[]
        for i in l:
            if i==900000000:
                g.append(9)
            else:
                g.append(1)
        k=10
        m = []
        for i in range(k + 1):
            m.append(0)
        cs = 0
        for i in range(n):
            cs = cs + g[i]
            m[((cs % k) + k) % k] = m[((cs % k) + k) % k] + 1
        r = 0
        for i in range(k):
            if (m[i] > 1):
                r = r + (m[i] * (m[i] - 1)) // 2
        r = r + m[0]

        print(r)
    break


