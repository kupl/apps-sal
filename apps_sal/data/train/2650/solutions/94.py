N, L = map(int, input().split())
s = []
for i in range(N):
    s.append(input())
print(''.join(sorted(s)))
