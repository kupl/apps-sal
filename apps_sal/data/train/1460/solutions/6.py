# cook your dish here
d, wage, tip = map(int, input().split())

arr = list(map(int, input().split()))

s = 0
wage_arr = [wage + tip*(1 - (1/50)*i) for i in range(6)]

for i in range(d):
    s += wage_arr[arr[i]-1]

if s >= 300:
    print("YES")
else:
    print("NO")
