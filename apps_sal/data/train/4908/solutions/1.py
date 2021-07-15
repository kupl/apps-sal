def epidemic(tm, n, s0, i0, b, a):
    timing = 0
    dt = tm/n
    r0 = 0
    i_max = i0
    while timing < tm:
        timing += dt
        s1 = s0 - dt*b*s0*i0
        i0 = i0 + dt*(b*s0*i0-a*i0)
        r0 = r0 + dt*r0*a
        s0=s1
        i_max=i0 if i0 > i_max else i_max
    return i_max
        
    # your code

