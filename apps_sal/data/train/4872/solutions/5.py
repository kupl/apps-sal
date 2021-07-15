class value:
 def __init__(s,x,y=0):s.x=getattr(x.x,s._)(y.x)if y else x
 def compute(s):return s.x
locals().update({p[2:-2]:type(p,(value,),{"_":p})for p in dir(int)if"_"==p[-2]})
