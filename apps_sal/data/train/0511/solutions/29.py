n=int(input())
a=[int(x) for x in input().split()]

tot=0
for i in range(n): tot^=a[i];
for i in range(n): a[i]^=tot;
print(*a)
