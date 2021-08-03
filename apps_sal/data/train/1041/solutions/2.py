t = int(input())
while(t):
    t = t - 1
    n = int(input())
    S = list(map(int, input().split()))
    max1 = -1 * float("inf")
    for i in range(len(S)):
        p = 1
        for j in range(i, len(S)):
            p = p * S[j]
            if max1 <= p:
                s_i = i
                s_f = j
                max1 = p
    print(max1, s_i, s_f)
