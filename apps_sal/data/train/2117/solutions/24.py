btqAIXPWRsBVCLo = int
btqAIXPWRsBVCLE = input
btqAIXPWRsBVCLp = list
btqAIXPWRsBVCLT = map
btqAIXPWRsBVCLN = range
btqAIXPWRsBVCLJ = max
btqAIXPWRsBVCLD = print
btqAIXPWRsBVCLy = str
btqAIXPWRsBVCLM = btqAIXPWRsBVCLo
btqAIXPWRsBVCLj = btqAIXPWRsBVCLE
btqAIXPWRsBVCLu = btqAIXPWRsBVCLp
btqAIXPWRsBVCLH = btqAIXPWRsBVCLT
btqAIXPWRsBVCLr = btqAIXPWRsBVCLN
btqAIXPWRsBVCLm = btqAIXPWRsBVCLJ
btqAIXPWRsBVCLa = btqAIXPWRsBVCLD
btqAIXPWRsBVCLf = btqAIXPWRsBVCLy
n = btqAIXPWRsBVCLM(btqAIXPWRsBVCLj())
r = [0]*(n+1)
a = [0]*(n+1)
a[1:-1] = btqAIXPWRsBVCLu(btqAIXPWRsBVCLH(btqAIXPWRsBVCLM,
                                          btqAIXPWRsBVCLj().split()))
s = [(0, 0)]
for i in btqAIXPWRsBVCLr(1, n+2):
    while a[i] < s[-1][0]:
        r[i-s[-2][1]-1] = btqAIXPWRsBVCLm(s[-1][0], r[i-s[-2][1]-1])
        del s[-1]
    s += [(a[i], i)]
for i in btqAIXPWRsBVCLr(n):
    r[-i-2] = btqAIXPWRsBVCLm(r[-i-2], r[-i-1])
btqAIXPWRsBVCLa(' '.join(btqAIXPWRsBVCLH(btqAIXPWRsBVCLf, r[1:])))

