RI = lambda : [int(x) for x in input().split()]
rw = lambda : [input().strip()]
n=int(input())
l=RI()

stack=[]
index_stack=-1

maxo=0
i=0
while(i<n):
    if(index_stack==-1 or stack[index_stack]>l[i]):
        stack.append(l[i])
        index_stack+=1
        i+=1
    else:
        #print(stack[index_stack],end=" ")
        #print(l[i])
        maxo=max(stack[index_stack]^l[i],maxo)
        temp=stack[index_stack]

        stack.pop()
        index_stack-=1

        
        if(len(stack)!=0):
            #print(stack[index_stack],end=" ")
            #print(stack[index_stack])
            maxo=max(temp^stack[index_stack],maxo)

while(len(stack)!=1):
    temp=stack[index_stack]
    
    stack.pop()
    index_stack-=1

    #print(stack[index_stack],end=" ")
    #print(stack[index_stack])
    maxo=max(temp^stack[index_stack],maxo)
print(maxo)

