from itertools import groupby

doc = { '1':'0', '0':'00' }

def send(s):
    return ''.join([' '.join( f'{doc[x[0]]} {"0"*x[1]}' for x in code( bit(s) ) )  ])
    
def code(e):
    return [(k,len(list(v))) for k,v in groupby(e)]
    
def bit(e):
    return ''.join( str(bin( ord(x) )[2:]).zfill(7) for x in e )
    
def receive(s):
    return ''.join( chr(int(e, 2)) for e in groups( encode( s.split(' ') ) , 7 ))

def encode(e):
    return ''.join( { v:k for k,v in list(doc.items()) }[e[0]] * len(e[1]) for e in groups(e,2)  )
        
def groups(e, d):
    return [ e[i:i+d] for i in range(0,len(e),d)]
    
    
    

