st,k=input().split()


k=int(k)
for i in range(len(st)):  
    if (k < 1):  
        break

    if (st[i] != '9'):  

        st = st[0:i] + '9' + st[i + 1:]  

        k -= 1
  
print(st)
