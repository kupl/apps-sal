def sort_two_arrays(arr1, arr2):
    arr1_,arr2_ = [[j,i] for i,j in enumerate(arr1)],[[j,i] for i,j in enumerate(arr2)]
    s, s1= sorted(arr1_,key=lambda x:(x[0],x[1])),sorted(arr2_,key=lambda x:(x[0],x[1]))
    return [[arr1[i[1]] for i in s1],[arr2[i[1]] for i in s]]
