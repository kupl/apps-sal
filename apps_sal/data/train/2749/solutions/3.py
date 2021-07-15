def solve(arr):
    print(arr)
    if arr==sorted(arr):
        return 'A'
    if arr==sorted(arr,reverse=True):
        return 'D'    
    if arr!=sorted(arr) and arr[-2]>arr[-1]:
        return 'RD'
    if arr!=sorted(arr) and arr[-2]<arr[-1]:
        return 'RA'


 

