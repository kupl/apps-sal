n = int(input())
a = list(map(int, input().split()))
all_xor = 0
for i in a:
    all_xor ^= i
l = []
for j in a:
    ans = all_xor ^ j
    l.append(ans)
print((*l))
