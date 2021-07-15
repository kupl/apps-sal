def invite_more_women(arr):
    cw=0
    cm=0
    for i in range(0,len(arr)):
        if arr[i]>0:
            cw=cw+1
        else:
            cm=cm+1
    if cm<cw:
        return True
    else:
        return False

