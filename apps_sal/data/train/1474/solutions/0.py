T = int(input())


def call_me(N, A, X):
    max = 0
    ans = ''
    for i in A:
        if i.count(X) > max:
            max = i.count(X)
            ans = i
    return ans


for i in range(T):
    N = int(input())
    A = list(map(str, input().split()))
    X = input()
    print(call_me(N, A, X))
