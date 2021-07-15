n, q = map(int, input().split())
a    = list(map(int, input().split()))
d    =  {}

def max_frequent(s, e, a):
    d = {}
    for x in a[s: e+1]:
        if x not in d:
            d[x] = 0
        d[x] += 1
        
    return e - s + 1 - max(list(d.values()))     
    
for i, x in enumerate(a):
    if x not in d:
        d[x] = []
    d[x].append(i)

segment = [[v[0], v[-1]] for v in d.values()]    
end     = -1
start   = -1 
block   = []

for s, e in segment:
    if s > end:
        if end != -1:
            block.append([start, end])
        start = s   
        end   = e 
    if e > end:
        end = e
        
block.append([start, end])        

cnt = 0
for s, e in block:
    cnt += max_frequent(s, e, a)
print(cnt)       
