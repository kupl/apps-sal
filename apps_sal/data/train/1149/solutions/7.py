from math import ceil


def isPalindrome(s, N):
    for i in range(ceil(N / 2)):
        if(s[i] != s[N - i - 1] and s[i] != '?' and s[N - i - 1] != '?'):
            return False
    return True


T = int(input())
ans = []
m = 10**7 + 9

for _ in range(T):
    S = input()
    N = len(S)

    if(isPalindrome(S, N)):
        count = 0
        for i in range(ceil(N / 2)):
            if(S[i] == '?' and S[N - 1 - i] == '?'):
                count += 1
        if(count == 0):
            ans.append(1)
        else:
            ans.append(((26 % m)**count) % m)
    else:
        ans.append(0)

for i in ans:
    print(i)
