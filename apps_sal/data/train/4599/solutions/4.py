def owl_pic(text):
    p = ''.join([i for i in text.upper() if i in ('8,W,T,Y,U,I,O,A,H,X,V,M')])
    return p + "''0v0''" + p[::-1]
