mapp={}
for _ in range(int(input())):
    data = input()
    new = [] 
    data=data.replace('u','oo')
    i=len(data)-1
    while i>=0:
        new.append(data[i])
        if data[i]=='h':
            i-=1
            while data[i]=='k':
                i-=1
        else:
            i-=1
    new=new[::-1]
    temp=''.join(new)
    if temp in mapp:
        mapp[temp]+=1
    else:
        mapp[temp]=1
print(len(mapp))

