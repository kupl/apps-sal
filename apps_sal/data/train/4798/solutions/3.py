import numpy as np
def avg_diags(m):
    m = np.array(m)
    md = m.diagonal() 
    sd = np.flipud(m).diagonal() 
    md = [md[i] for i in range(1,len(md),2) if md[i]>=0]
    sd = [sd[i] for i in range(0,len(sd),2) if sd[i]<0]
    avs = -1
    if sd:
        avs = round(abs(sum(sd))/len(sd))
    return [round(sum(md)/len(md)),avs ] 
