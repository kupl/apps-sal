def tops(msg):
    r=[]
    for i in range(int(1+(-1+(1+2*len(msg))**0.5)*0.5),0,-1):
        r.append(msg[(i*2-1)*(i+1):i*(i+1)*2])
    return ''.join(r)
