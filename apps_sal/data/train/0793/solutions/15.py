# cook your dish here
n,r = map(int,input().split())
h = list(map(int,input().split()))
if r not in h:
    h.append(r)
h.sort()
d = [abs(h[i+1] - h[i]) for i in range(n-1)]
m = max(d)
ans = 0
for i in range(m,0,-1):
    if any([j%i!=0 for j in d]):
        continue
    else:
        ans = i
        break
print(ans)
