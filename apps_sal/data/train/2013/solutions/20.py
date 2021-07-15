import sys
slowo = input()
slowo=slowo+'a'
ret = ""
i =0
while slowo[i]=="a" and len(slowo)>i+1:
    i+=1
    ret+='a'
if i+1==len(slowo):
    w=slowo[0:len(slowo)-2]+'z'
    print (w)
    return
while slowo[i]!='a' and len(slowo)>i:
    ret=ret+chr(ord(slowo[i])-1)
    i+=1
ret=ret+slowo[i:len(slowo)-1]
print(ret)
