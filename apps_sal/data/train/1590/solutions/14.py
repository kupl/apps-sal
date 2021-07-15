for i in range(int(input())):
          
    l=[int(x) for x in input().split()]
    
    l.sort(reverse=True)
    if(l[1]+l[2]>=l[0]):
       print("Yes") 
    else:
       print("No") 
