t = int(input())
s = list(map(int, input().split()))
i = 0
j = t
revenue = 0

for i in range(t-1) : 
    for j in range(i+1, t) :
        revenue += ((s[i]>s[j])*((2*s[i])-(2*s[j])) + s[j]-s[i])

print(revenue)
