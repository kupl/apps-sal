def invite_more_women(arr):
    N=len(arr)
    w,m=0,0
    for i in range(N):

        if arr[i] == -1:
            w+=1
        elif arr[i] == 1:
            m+=1
    if m>w:
        return True
    else:
        return False
