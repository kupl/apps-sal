import numpy as np
def distribute(nodes, workload):
    lst=[]
    value = 0
    for i in range(nodes):
        length = int(np.ceil((workload-value)/(nodes-i)))
        lst.append([l for l in range(value,value+length)])
        value = value + length
    return lst
