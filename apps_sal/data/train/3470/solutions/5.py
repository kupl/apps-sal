to_twos_complement=lambda s,l:int(s.replace(' ',''),2)if s[0]=='0'else-(int("".join([str(int(i)^1)for i in s.replace(' ','')]),2)+1)
from_twos_complement=lambda n,b:bin(n&0xffffffffffffffffffff)[2:][-b:]if n<0else bin(n)[2:].zfill(b)
