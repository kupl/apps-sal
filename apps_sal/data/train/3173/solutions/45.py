def create_array(n):
    res = []
    i = 0
    while i <= n: 
        i += 1
        res.append(i)
        if i == n:
            return res
        
r = create_array(1)
print(r)
