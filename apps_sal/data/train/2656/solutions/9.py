def bird_code(arr):
    arr1=[s.replace('-',' ') for s in arr]
    res=[]
    for s in arr1:
        arr2=s.split(' ')
        if len(arr2)==1:
            res.append(arr2[0][:4].upper())
        elif len(arr2)==2:
            res.append(arr2[0][:2].upper()+arr2[1][:2].upper())
        elif len(arr2)==3:
            res.append(arr2[0][0].upper()+arr2[1][0].upper()+arr2[2][:2].upper())
        else:
             res.append(arr2[0][0].upper()+arr2[1][0].upper()+arr2[2][0].upper()+arr2[3][0].upper())
    return res
