'''Author- Akshit Monga'''
from sys import stdin, stdout
input = stdin.readline


def val(i):
    if i == '?':
        return 26
    return ord(i) - 97


t = int(input())
for _ in range(t):
    s = input()[:-1]
    ans = 0
    mask = 0
    for i in s:
        if i == '?':
            continue
        mask ^= (1 << val(i))
    hash = {0: 1}
    pre = 0
    for i in s:
        pre ^= (1 << val(i))
        ans += hash.get(pre ^ mask, 0)
        x = mask ^ (1 << 26)
        for j in range(26):
            ans += hash.get(pre ^ (1 << j) ^ x, 0)
        hash[pre] = hash.get(pre, 0) + 1
    stdout.write(str(ans) + '\n')
