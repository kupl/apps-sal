def skrzat(t, i):
    return "From binary: "+str(i)+" is "+str((2863311530^int(i,2))-2863311530) if t=='b' else "From decimal: "+str(i)+" is "+str(bin((2863311530+i)^2863311530))[2:]
