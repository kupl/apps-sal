def change_count(change):
    a=change.split(" ")
    L=[]
    for i in range(len(a)):
        if a[i]=="penny":
            L.append(0.01)
        elif a[i]=="nickel":
            L.append(0.05)
        elif a[i]=="dime":
            L.append(0.10)
        elif a[i]=="quarter":
            L.append(0.25)
        elif a[i]=="dollar":
            L.append(1.000)
    b=sum(L)
    x=round((b+0.0000001),2)
    a='$'+("%.2f"%x)
    y=a.split()
    if len(y)==4:
        y.append('0')
        return sum(y)
    else:
        return a
