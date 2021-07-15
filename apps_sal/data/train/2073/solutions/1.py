n = int(input())
Ar = [int(x)for x in input().split()]
stack = []
ans = 0
for i in range(0,n):
    while(len(stack)!=0):
        if(stack[-1]<Ar[i]):
            ans = max(ans,stack[-1]^Ar[i])
            stack.pop()
        else:
            ans = max(ans,stack[-1]^Ar[i])
            break
    stack.append(Ar[i])
print(ans)

