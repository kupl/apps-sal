def hex_color(codes):
    r,g,b = [ int(hex) for hex in (codes.split(' ') if codes != '' else '000') ]
    m = max(r,g,b)
    return ['black','red','green','yellow','blue','magenta','cyan','white'][(m>0) * ( 1*(r==m) + 2*(g==m) + 4*(b==m) )]
