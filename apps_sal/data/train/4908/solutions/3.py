def epidemic(tm, n, s0, i0, b, a):
    dt = tm/float(n); t = [0] * (n+1)
    s = [0] * (n+1); i = [0] * (n+1); r = [0] * (n+1)
    s[0] = s0; i[0] = i0; r[0] = 0; t[0] = 0
    for k in range(n):
        t[k+1] = (k+1)*dt
        s[k+1] = s[k] - dt*b*s[k]*i[k]
        i[k+1] = i[k] + dt*(b*s[k]*i[k] - a*i[k])
        r[k+1] = r[k] + dt*i[k]*a
    return int(max(i))
