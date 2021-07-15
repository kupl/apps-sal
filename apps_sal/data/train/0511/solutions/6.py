n = int(input())
a = list(map(int,input().split()))
sub = 0
for i in range(n):
    sub ^= a[i]

for i in range(n):
    print(sub ^ a[i],end = ' ')


