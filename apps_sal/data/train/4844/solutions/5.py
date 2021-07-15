def get_password(grid,directions):
    m_go = { 'left':(0,-1), 'right':(0,1), 'up':(-1,0), 'down':(1,0)  }
    
    x,y = next((i,j) for i, e in enumerate(grid) for j, l in enumerate(e) if l == 'x')
                
    password = ''
    
    for e in directions:
        (x_,y_), end = m_go.get(e.strip('T')), e[-1]
        x, y = x+x_, y+y_
        if end is 'T':
            password += grid[x][y]
    
    return password

