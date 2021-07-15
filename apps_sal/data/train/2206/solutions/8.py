n = int(input())
x = [0]*n
a = 0
p = list(map(int, input().split()))
z = n-1
ans = ['1']
for i in range(n):
    x[p[i]-1] = 1
    a += 1
    while z> -1 and x[z] == 1:
        z-=1
        a-=1
    ans.append(str(a+1))
print(' '.join(ans))
