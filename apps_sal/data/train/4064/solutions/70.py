def count_by(n, x):
    results=[]
    s=n
    for i in range (1, x+1):
        results.append(s)
        s=s+n
    return results
