def friend(x):
   
#set an empty list to fill the output with
    result=[]
   
#make a forloop to go through the list and add the names that have 4 letter to result
    for i in x:
        if len(i) == 4:
            result.append(i)

    
    return(result)
    

