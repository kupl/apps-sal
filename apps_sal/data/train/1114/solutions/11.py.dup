# cook your dish here
try:
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        c = 0
        d = []
        for i in range(N):
            for j in range(i + 1, N):
                d.append(A[i] + A[j])
        ans = d.count(max(d)) / len(d)
        print('%0.8f' % ans)
except:
    pass
