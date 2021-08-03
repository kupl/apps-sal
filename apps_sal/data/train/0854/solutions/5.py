# cook your dish here
def pure_it(L, N):
    for j in range(1, N):
        if L[j - 1] == L[j]:
            return 'ne krasivo'
    return 'prekrasnyy'


t = int(input())
for i in range(t):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    print(pure_it(L, N))
