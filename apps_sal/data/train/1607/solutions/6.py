n=input()
i=0
for x in range(len(n)):
    if n[x]=='Q':
        for y in range(x,len(n)):
            if n[y]=='A':
                for z in range(y,len(n)):
                    if n[z]=='Q':
                        i+=1
print(i)

