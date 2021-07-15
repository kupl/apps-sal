def find_slope(p):
    x = p[3]-p[1]
    y = p[2]-p[0]
    
    if y==0:
       return "undefined"
    else:
       return "{}".format(int(x/y))
    
    

