Test = input()
T = int(Test)
L = []
for t in range(T):
    Num = input()
    N = int(Num)
    L.append(N)
L.sort()
Leng = len(L)
for l in range(Leng):
    print(L[l])
