# cook your dish here
# cook your dish here
for case in range(int(input())):
    n=int(input())
    
    k=1
    i=1
    for i in range(0,n):
        for j in range(0,n):
            k+=1
            print(k,end="")
        k=2
        k+=i
        i+=1
        print("")
        

