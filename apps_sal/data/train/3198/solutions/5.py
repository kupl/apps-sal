def check_exam(arr1,arr2):
    k=0; #a place in memory where we shall store the points
    for x in range(len(arr1)): #lets check every answer in the array
        if arr2[x]!='': #and if the answer is not empty
            if arr1[x]==arr2[x]: k+=4 #we will give +4 point for the correct answer
            else: k-=1 #and -1 for any other (incorect) answers
    if k<1: return 0 #if we have 0 ot negative points we should return just zero
    #so we dont embarice further the poor students
    return k
