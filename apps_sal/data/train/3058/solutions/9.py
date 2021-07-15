def is_magical(sq):
    a,b,c, j,k,l, x,y,z = sq
    return a+b+c==j+k+l==x+y+z==a+j+x==b+k+y==c+l+z==a+k+z==c+k+x
