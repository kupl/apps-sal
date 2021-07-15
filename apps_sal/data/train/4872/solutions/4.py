class value:
 def __init__(s,a,b=0):
  s.v=a
  if b!=0:s.v={add:a.v+b.v,sub:a.v-b.v,mul:a.v*b.v,truediv:a.v/b.v,mod:a.v%b.v,pow:a.v**b.v}[type(s)]
class v(value):  
 def compute(s):return s.v
class add(v):1
class sub(v):1
class mul(v):1
class truediv(v):1
class mod(v):1
class pow(v):1
