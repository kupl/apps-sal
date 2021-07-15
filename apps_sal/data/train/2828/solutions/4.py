power_law=lambda a,b,x:round(a[1]*(b[1]/(a[1]+1e-9))**__import__('math').log(x/(a[0]+1e-9),b[0]/(a[0]+1e-9)))
