# cook your dish here
for _ in range(int(input())):
    N = int(input().strip())
    A = list(map(int, input().split()))
    m1 = 0
    ma = 0
    mc = 1
    for i in range(N):
        if A[i] == 1:
            ma = ma + 1
            if ma > 1 and m1 < 5:
                mc = 0
                print("NO")
                break
            m1 = 0
        else:
            m1 = m1 + 1
    #     print(i, A[i], ma, m1)
    if mc == 1:
        print("YES")
