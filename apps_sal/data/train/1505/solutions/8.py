# cook your dish here
N = int(input())

enc = input().split()
S = []

for e in enc : 
    if e == "1" : S.append("(")
    else : S.append(")")



# task 1 : max depth 

closures = []
d = 0
max_d = 0
max_d_idx = 0
start = 0
for idx in range(N) :
    
    
    s = S[idx]
    if s == "(" : 

        d += 1
        
        if d > max_d : 
            max_d = d 
            max_d_idx = idx + 1
        
    else : 
        d -= 1
    
    if d == 0 : 
        finish = idx
        closures.append([start, finish])
        start = idx + 1
    
    
    
    
# task 2 : maximum closure


diff = [x[1] - x[0] for x in closures]
max_diff = max(diff)
max_diff_idx = closures[diff.index(max_diff)][0] + 1


        
print(max_d, max_d_idx, max_diff + 1, max_diff_idx)
