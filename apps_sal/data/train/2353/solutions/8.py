n = int(input())
L = list(map(int, input().split()))
S = sorted(L)
for i in L:
    print(S[(S.index(i) + 1)%n], end=' ')
