def get_diagonale_code(grid: str) -> str:
    if not grid:
        return ''
    s=[]    
    for line in grid.split('\n'):
        s.append(line.split(' '))
    if len(s)==1:
        return s[0][0]
    x,y=0,0
    m=-1
    r=''
    while(y<len(s[x])):
        r+=s[x][y]
        if x==0 or x==len(s)-1:
            m*=-1
        x+=m
        y+=1
    return r
