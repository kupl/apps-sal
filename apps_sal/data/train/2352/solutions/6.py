s = input()
if(s[0]=='h'):
    s = s[:4]+'://'+s[4:]
else:
    s = s[:3]+'://'+s[3:]
f=s.find("ru",s.find("://")+4)
s=s[:f]+"."+s[f:]
if(len(s)-f>3):
    s=s[:f+3]+'/'+s[f+3:]
print(s)


