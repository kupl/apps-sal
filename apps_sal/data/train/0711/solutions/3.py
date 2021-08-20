"""Author- Akshit Monga"""
from sys import stdin, stdout
input = stdin.readline
t = int(input())
for _ in range(t):
    s = input()[:-1]
    n = len(s)
    mask = [0 for i in range(26)]
    for i in s:
        if i == '?':
            continue
        mask[ord(i) - 97] ^= 1
    good = [mask + [0]]
    for i in range(26):
        temp = mask.copy()
        temp[i] ^= 1
        good.append(temp + [1])
    pre_masks = {'0' * 27: 1}
    temp = [0 for i in range(27)]
    ans = 0
    for i in range(n):
        if s[i] == '?':
            temp[26] ^= 1
        else:
            temp[ord(s[i]) - 97] ^= 1
        good1 = mask + [0]
        xor = ''
        for j in range(27):
            xor += str(temp[j] ^ good1[j])
        if xor in pre_masks:
            ans += pre_masks[xor]
        good2 = mask + [1]
        xor1 = ''
        for j in range(27):
            xor1 += str(temp[j] ^ good2[j])
        for j in range(26):
            xor2 = xor1[:j] + str(int(xor1[j]) ^ 1) + xor1[j + 1:]
            if xor2 in pre_masks:
                ans += pre_masks[xor2]
        pre = ''.join([str(e) for e in temp])
        if pre in pre_masks:
            pre_masks[pre] += 1
        else:
            pre_masks[pre] = 1
    stdout.write(str(ans) + '\n')
