tc=int(input())
for q in range(tc):
        arr=input()
        stack=[]
        maxx=0
        counter=0
        for i in arr:
            
            counter+=1
            if(i=='<'):
                stack.append(i)
            elif(i=='>' and len(stack)):
                stack.pop()
                if(not stack):
                       maxx=counter
            else:
                  break
        print(maxx)
