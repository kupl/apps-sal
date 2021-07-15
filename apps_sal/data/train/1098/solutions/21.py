t=int(input())
for i in range(t):
 n=int(input())
 l=sorted(map(int, input().split()), reverse=True)
 print(sum(l[::2]))
