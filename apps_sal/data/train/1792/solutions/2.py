a=[1];b=[0];c=[0];d=[0];e=[0];f=[0]
for _ in range(10000):
    aa=b[-1]+c[-1]+f[-1]
    bb=a[-1]+d[-1]
    cc=a[-1]+e[-1]
    dd=b[-1]
    ee=c[-1]
    ff=a[-1]

    a.append(aa%12345787)
    b.append(bb%12345787)
    c.append(cc%12345787)
    d.append(dd%12345787)
    e.append(ee%12345787)
    f.append(ff%12345787)

def three_by_n(n):
    if n%2==0: return a[n]
    tot=0
    for i in range(n):
        tot += d[i]*a[n-i-1] + a[i]*d[n-i-1] + b[i]*b[n-i-1] + a[i]*a[n-i-1]
        tot %= 12345787
    return (2*tot) % 12345787
