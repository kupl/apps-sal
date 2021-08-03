# cook your dish here
# cook your dish here
n = 0
m = 0
A = []
B = []
anscount = 0
k = 0


def generate(n, m, l):
    nonlocal anscount
    if(len(l) == n + m):
        X = l
        i, j = 0, 0
        C = [0 for t in range(n + m)]
        while((i + j) < (n + m)):
            if(X[i + j] == 0):
                C[i + j] = A[i]
                i = i + 1
            else:
                C[i + j] = B[j]
                j = j + 1
        ans = len(C)
        for i in range(1, len(C)):
            if(C[i] == C[i - 1]):
                ans -= 1
        if(ans == k):
            anscount += 1
    else:
        if(l.count(1) < m):
            generate(n, m, l + [1])
            if(l.count(0) < n):
                generate(n, m, l + [0])
        else:
            if(l.count(0) < n):
                generate(n, m, l + [0])


for _ in range(int(input())):
    anscount = 0
    n, m, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    generate(n, m, [])
    print(anscount)
