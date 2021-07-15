# cook your dish here
t=int(input());
A=0
for i in range(t):
    s=input().lower();
    c=0;
    e='';
    for i in range(len(s)):
        if s[i]==' ':
            c=c+1;
    #print(c);
    for i in range(len(s)):
        if c==0:
            print(s[0].upper()+s[1:]);
            break;
        elif c==1:
            if s[i]==' ':
                print(s[0].upper()+'.'+' '+s[i+1].upper()+s[i+2:]);
                break;
        elif c==2:
            if s[i]==' ':
                A=i;
                #print(A)
                f=s[i+1].upper();
                e=e+f;
        
    if c==2:
        print(s[0].upper()+'.'+' '+e[0]+'.'+' '+e[1]+s[A+2:]);
           
           
                
                
                
                
                
                
    
        
        

