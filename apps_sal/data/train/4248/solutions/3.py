def solve(files):
    if not files:
        return files
    
    d = {}
    
    for file in files:
        ext = file.split('.')[-1]
        
        if ext in d:
            d[ext] += 1
        else:
            d[ext] = 0
            
    m = max(d.values())
    
    most_used = ['.'+i for i, j in list(d.items()) if j == m]
    
    return sorted(most_used)

