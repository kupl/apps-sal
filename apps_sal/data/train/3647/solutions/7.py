def solve(arr):
    arr=sorted(arr)
    arr.append(0)
    arr=sorted(arr)
    list1 = []
    for i in range(1,len(arr)//2+2):
        list1.append(arr[-i])
        list1.append(arr[i])
    list1=list(dict.fromkeys(list1))
    return list1

