def median(arr):
    arr.sort()
    return (arr[(len(arr) - 1)//2] + arr[(len(arr))//2])/2
