def paul(x):
    points=sum({"kata":5,"Petes kata":10,"life":0,"eating":1}[v] for v in x)
    return [[["Miserable!","Sad!"][points<100],"Happy!"][points<70],"Super happy!"][points<40]
