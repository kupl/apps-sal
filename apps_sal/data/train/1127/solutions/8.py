# cook your dish here
t=int(input())
for _ in range(t):
    name=input()
    name.lower()
    list_nm=name.split()
    k=len(list_nm)
    
    if(k==1):
        print(name.title())
    else:
        
        

        for i in list_nm[:k-1]:
            print(i[:1].title()+ '.',end=' ')
        print(list_nm[k-1].title())

