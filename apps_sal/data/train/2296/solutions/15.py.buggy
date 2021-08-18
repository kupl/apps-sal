from collections import deque
alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

S = input()
N = len(S)

dic = {moji: deque([]) for moji in alphabetlist}
for i in range(N):
    dic[S[i]].append(i + 1)

left = deque([])
right = deque([])
mid = []

if N % 2 == 1:
    check = 0
    memo = 0
    for moji in dic:
        if len(dic[moji]) % 2 == 1:
            k = len(dic[moji])
            check += 1
            memo = dic[moji][k // 2]
    if check != 1:
        print(-1)
        return
    else:
        mid.append(memo)
else:
    check = 0
    for moji in dic:
        if len(dic[moji]) % 2 == 1:
            print(-1)
            return

for i in range(N // 2):
    for moji in alphabetlist:
        if len(dic[moji]) >= 2:
            L = dic[moji][0]
            R = dic[moji][-1]
            for moji2 in alphabetlist:
                if len(dic[moji2]) >= 2 and dic[moji2][0] < L < R < dic[moji2][-1]:
                    break
            else:
                left.append(L)
                right.appendleft(R)
                dic[moji].popleft()
                dic[moji].pop()
                break

ans = list(left) + mid + list(right)
n = N
# A1 ... AnのBIT(1-indexed)
BIT = [0] * (n + 1)

# A1 ~ Aiまでの和 O(logN)


def BIT_query(idx):
    res_sum = 0
    while idx > 0:
        res_sum += BIT[idx]
        idx -= idx & (-idx)
    return res_sum

# Ai += x O(logN)


def BIT_update(idx, x):
    while idx <= n:
        BIT[idx] += x
        idx += idx & (-idx)
    return


res = 0
for i in range(N):
    res += i - BIT_query(ans[i])
    BIT_update(ans[i], 1)

print(res)
