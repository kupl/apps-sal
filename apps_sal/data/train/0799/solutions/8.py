# cook your dish here
ans = 0
for i in range(int(input())):
 if sum(list(map(int,input().split()))) >= 2: ans += 1
print(ans)
