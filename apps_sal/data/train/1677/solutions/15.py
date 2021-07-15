# cook your dish here
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
prev = [0]*1000006
summ = [0]*1000006
diff = [0]*1000006
prev[0] = b[0]
for i in range(n):
    res = max(res,a[i])
for i in range(1,n):
    prev[i] = b[i] + prev[i-1]
summ[0] = a[0] 
diff[0] = a[0] = prev[0]
for i in range(n):
    diff[i] = max(diff[i-1],a[i]-prev[i])
for i in range(n):
    summ[i] = max(summ[i],a[i]+prev[i-1])
for i in range(n):
    res = max(res,a[i]+prev[i-1]+diff[i-1])
for i in range(n):
    res = max(res,a[i] + prev[n-1] +summ[i-1]-prev[i])
print(res)
