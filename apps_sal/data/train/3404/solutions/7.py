def solve(st,a,b):
    c = st[a:b+1]
    front = st[:a]
    back = st[b+1::]
    
    everything =  front + c[::-1] + back
    return everything
