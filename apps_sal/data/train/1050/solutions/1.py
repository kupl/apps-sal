# cook your dish here
for y in range(int(input())):
    s=input()
    st=[]
    i=-1
    a=0
    for x in range(len(s)):

        if i==-1 and s[x]=='>':
            
            break
        elif s[x]=='<':
            st.append('<')
            i+=1
        elif s[x]=='>':
            st.pop()
            i-=1
        if i==-1:
            a=x+1
    print(a)
        
            
    
            
            
