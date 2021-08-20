def isPalindrome(S, N):
    for i in range(N):
        if S[i] != S[N - 1 - i]:
            return False
    return True


T = int(input())
ans = []
for _ in range(T):
    S = input()
    N = len(S)
    if isPalindrome(S, N):
        ans.append(1)
    else:
        ans.append(2)
for i in ans:
    print(i)
