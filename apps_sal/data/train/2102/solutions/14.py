# https://codeforces.com/contest/232/problem/A
# WA 

def f_3(n):
    return n * (n-1) * (n-2) // 6

def f_2(n):
    return n * (n-1) // 2

a_3   = [f_3(i) for i in range(100)]
a_2   = [f_2(i) for i in range(100)]

def find_2(x, a):
    arr = []
    cur = len(a) - 1
    
    while x > 0:
        while x < a[cur]:
            cur -= 1
        arr.append(cur)
        x -= a[cur]
        
    return arr

def find_3(x, a):
    cur = len(a) - 1
    
    while x < a[cur]:
        cur -= 1
    
    x -= a[cur]

    return cur, x    

def build(x):
    base, remain = find_3(x, a_3)
    arr          = find_2(remain, a_2)
    
    n  = base 
    #print(base, arr)
    
    if len(arr) > 0:
        n += len(arr)
        
    m  = [[0]*n for _ in range(n)]

    for i in range(base):
        for j in range(base):
            if i == j:
                continue
            m[i][j] = 1
            m[j][i] = 1
        
    for i, x in enumerate(arr):
        for j in range(x):
            m[base+i][j] = 1
            m[j][base+i] = 1
        
    return m        

def pr(m):
    for i in range(len(m)):
        print(''.join([str(x) for x in m[i]]))

k  = int(input())
m  = build(k)

print(len(m))
pr(m)
