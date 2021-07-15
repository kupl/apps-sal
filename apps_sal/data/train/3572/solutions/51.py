def invite_more_women(arr):
    x=sum(i for i in arr)
    if 2<=len(arr)<=50:
        if x>0:
            return True
        else: return False
    else: return False
