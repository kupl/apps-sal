# cook your dish here
tcase=int(input())
for i in range(tcase):
    ninput=input()
    nlist=list(ninput.split(" "))
    A=[]
    B=[]
    numinput=input()
    A=list(numinput.split(" "))
    B=A*int(nlist[1])
    size=int(nlist[0])*int(nlist[1])
    B=[int(i) for i in B]
    max_so_far =B[0] 
    curr_max = B[0] 
    for i in range(1,size): 
        curr_max = max(B[i], curr_max + B[i]) 
        max_so_far = max(max_so_far,curr_max) 
          
    print(max_so_far) 

