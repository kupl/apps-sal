# cook your dish here
t=int(input())
while t:
    t-=1
    
    s= str(input())
    
    while (len(s)>0 and  s.find('abc')!=-1):
        s=s.replace('abc','')
    
    print(s)
    

