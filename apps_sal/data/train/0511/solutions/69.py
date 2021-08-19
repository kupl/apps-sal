N = int(input())
a = list(map(int, input().split()))
b = 0
for i in a:
    b ^= i
ans = []
for i in a:
    ans.append(b ^ i)
print(' '.join(map(str, ans)))
