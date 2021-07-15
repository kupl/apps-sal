def ex_euler(n):
    import numpy as np
    n_steps = n+1
    T=1
    t = np.linspace(0,T,n_steps)
    h=T/n
    zk = 1+0.5*np.exp(-4*t)-0.5*np.exp(-2*t)
    yk = [1]
    
    for i in range(1,n_steps):
        dy_dt = 2 - np.exp(-4*t[i-1])-2*yk[i-1]
        yk.append(yk[i-1]+dy_dt*h)
        
    err = np.divide(np.abs(np.array(yk) - zk),zk)
    err = str(np.sum(err)/(n+1))
    err = float(err[:err.find('.')+7])
    return err
    

