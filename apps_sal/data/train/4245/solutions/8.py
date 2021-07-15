def explode(arr):
    score=0
    if isinstance(arr[0],int):
        score+=arr[0]
    if isinstance(arr[1],int):
        score+=arr[1]
    if score==0:
        return 'Void!'
    return list([arr]*score)
