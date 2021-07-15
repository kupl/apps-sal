
def mod(a,b):
    r = a % b;
    r = r+b if(r < 0) else r
    print(r)
    return r

def ColorToInt(c):
    if c == 'R': 
        return 0
    if c=='G': 
        return 1
    if c == 'B': 
        return 2
    return -1
    

def IntToColor(i):
    if i == 0: 
        return 'R'
    if i==1: 
        return 'G'
    if i == 2: 
        return 'B'
    return 'E'

def triangle(row):
    end = len(row)-1
    i=0
    seq = list(row)
    while(end > 0):
        seq[i] = IntToColor( mod(-ColorToInt(seq[i])-ColorToInt(seq[i+1]), 3)  );
        i+=1;
        if i == end:
            end-=1;  
            i = 0; 
        
    return seq[0]

