s = input()
cnt = [0] * 26
n = len(s)

for c in s:
    cnt[ord(c) - ord('a')] += 1

odd = -1
for i in range(26):
    if cnt[i] % 2 == 1:
        if odd != -1:
            print(-1)
            return
        odd = i

cnt2 = [[] for i in range(26)]
nums = []
left = 0
for i in range(len(s)):
    c = s[i]
    ind = ord(c) - ord('a')
    if len(cnt2[ind]) * 2 + 1 == cnt[ind]:
        cnt2[ind].append((n-1)//2)
        nums.append((n-1)//2)
    elif len(cnt2[ind]) <= (cnt[ind]-1)//2:
        cnt2[ind].append(left)
        nums.append(left)
        left += 1
    else:
        num = n - 1 - cnt2[ind][cnt[ind]-1-len(cnt2[ind])]
        cnt2[ind].append(num)
        nums.append(num)

ans = 0
#print(nums)
bit = [0] * (n+1)
def add(x):
    nonlocal bit
    x += 1
    while x <= n:
        bit[x] += 1
        x += x & -x

def sum(x):
    x += 1
    res = 0
    while x:
        res += bit[x]
        x -= x & -x
    return res
for num in nums[::-1]:
    ans += sum(num)
    add(num)

print(ans)
