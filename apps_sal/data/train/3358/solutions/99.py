def correct(string):
    arr=[]
    for i in string:
        arr.append(i)
    res=""
    for i in range(0,len(arr)):
        if arr[i]=="0":
            arr[i]="O"
        if arr[i]=="5":
            arr[i]="S"
        if arr[i]=="1":
            arr[i]="I"
        res+=arr[i]
    return res
