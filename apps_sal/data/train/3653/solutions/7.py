def tops(msg):
    return "".join(msg[(i*2-1)*(i+1):i*(i+1)*2] for i in range(int(1+(-1+(1+2*len(msg))**0.5)*0.5),0,-1))
