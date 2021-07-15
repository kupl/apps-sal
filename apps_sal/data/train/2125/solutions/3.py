# https://codeforces.com/problemset/problem/848/B

def push(d, val, type_, arr):
    # pos index
    type_ %= 2
    if val not in d:
        d[val] = [[],[]]
    d[val][type_].append(arr)

d = {}

n, w, h = map(int, input().split())
for index in range(n):
    g, p, t = map(int, input().split())
    push(d, p-t, g, [p ,index])
    
for k, v in d.items():
    v[0]=sorted(v[0], key = lambda x: x[0], reverse=True)
    v[1]=sorted(v[1], key = lambda x: x[0], reverse=False)
    
ans = [0] * n

for v in d.values():
    cur=0
    bound = len(v[1])
    step  = len(v[0])
    merge = v[0]+v[1]
    n_    = len(merge)

    for pos, index in merge:
        if cur<bound:
            ans[index]=str(merge[(step+cur)%n_][0])+' '+str(h)
        else:
            ans[index]=str(w)+' '+str(merge[(step+cur)%n_][0])
        cur+=1    
print('\n'.join(ans))    
