import math
def predict_age(q, w, e, r, t, y, u, i):
    x = [q,w,e,r,t,y,u,i]
    for i,j in enumerate(x):
        x[i] = j*j
    return int(str(math.sqrt(sum(x))/2).split(".")[0])
