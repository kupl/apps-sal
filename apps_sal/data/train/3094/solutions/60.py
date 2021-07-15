def sum_array(arr):
    if arr==None:
        return 0
    
    elif len(arr)==1:
        return 0
    elif arr==[]:
        return 0
    else:
        somme = 0
        for elements in arr:
            somme+=elements
        
        somme=somme-min(arr)-max(arr)
            
        return somme

