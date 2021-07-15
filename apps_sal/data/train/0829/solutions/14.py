t = int(input())
s = list(map(int, input().split()))
revenue = 0
s.sort()
s.reverse()

for i in range(t) :
    revenue -= i * s[i]
    revenue += (t - i - 1) * s[i]
    
print(revenue)
