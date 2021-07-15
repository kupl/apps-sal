from functools import reduce
def hex_to_dec(s):
    d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    return reduce(lambda x,y:x*16+d[y],s,0)
