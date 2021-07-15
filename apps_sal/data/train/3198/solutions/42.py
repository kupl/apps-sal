def check_exam(arr1,arr2):
    if check0(arr1, arr2)+check1(arr1, arr2)+check2(arr1, arr2)+check3(arr1, arr2)+minus(arr1, arr2)<0:
        return 0
    else:
        return check0(arr1, arr2)+check1(arr1, arr2)+check2(arr1, arr2)+check3(arr1, arr2)+minus(arr1, arr2)
        
def minus(arr1, arr2):
    arr0=[i for i in arr2 if len(i)==0]
    return 0*len(arr0)

def check0(arr1, arr2):
    if arr1[0]==arr2[0]:
        return +4
    else:
        if len(arr2[0])==0:
            return 0
        else:
            return -1
        
def check1(arr1, arr2):
    if arr1[1]==arr2[1]:
        return +4
    else:
        if len(arr2[1])==0:
            return 0
        else:
            return -1
        
def check2(arr1, arr2):
    if arr1[2]==arr2[2]:
        return +4
    else:
        if len(arr2[2])==0:
            return 0
        else:
            return -1
    
def check3(arr1, arr2):
    if arr1[3]==arr2[3]:
        return +4
    else:
        if len(arr2[3])==0:
            return 0
        else:
            return -1
