n=int(input())

a=[int(x) for x in input().split()]
k,d=0,0
st=[]

st.append(a[0])
k,d=1,1
for i in range(1,n):
    if a[i]==1 or a[i]==3:
        st.append(a[i])

        if st[len(st)-1]!=st[len(st)-2]:
            k+=1
            if k>d:
                d+=1
        #print(st,k,d)
    else:
        try:
            if st[len(st)-1]!=st[len(st)-2]:
                k-=1
            st.pop()
        except:
            st.pop()
            k-=1
        #print(st,k,d)

c1,max1=0,0
s1=[]
for i in range(n):
    try:
        if len(s1)==0 and a[i]==1:
            s1.append(a[i])
            c1+=1
        elif len(s1)!=0 and (a[i]==1 or a[i]==3):
            s1.append(a[i])
            c1+=1

        elif a[i]==2 or a[i]==4:
            s1.pop()
            c1+=1
        if max1 < c1:
            max1 = c1
        if len(s1)==0:
            c1=0
    except:
        pass



c2,max2=0,0
s2=[]
for i in range(n):
    try:
        if len(s2)==0 and a[i]==3:
            s2.append(a[i])
            c2+=1
        elif len(s2)!=0 and (a[i]==1 or a[i]==3):
            s2.append(a[i])
            c2+=1

        elif a[i]==2 or a[i]==4:
            s2.pop()
            c2+=1
        if max2 < c2:
            max2 = c2
        if len(s2)==0:
            c2=0
    except:
        pass

print(d,max1,max2)

