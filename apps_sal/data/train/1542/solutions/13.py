# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    N = [int(i) for i in input().split()]
    dic = {'.': 1, 'd': 2, 't': 3, 'D': 1, 'T': 1}
    maxx = 0
    for i in range(n - 8 + 1):
        st = s[i:i + 8]
        total = 0
        D = 0
        T = 0
        for j in range(8):
            if st[j] in ['.', 'd', 't']:
                total = total + dic[st[j]] * N[j]
            elif st[j] == 'D':
                total = total + dic[st[j]] * N[j]
                D = D + 1
            else:
                total = total + dic[st[j]] * N[j]
                T = T + 1
        total = total * (2**D)
        total = total * (3**T)
        if maxx < total:
            maxx = total
    print(maxx)
