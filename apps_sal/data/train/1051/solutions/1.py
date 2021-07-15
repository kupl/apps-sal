# cook your dish here
n=int(input())
for i in range(n):
    k=int(input())
    for j in range(0,k+1):
        for l in range(0,j+1):
            
            if j==0:
                print(j)
            elif l<j:
                print("*",end="")
            elif l==j:
                print(l)
    print("\n")        
