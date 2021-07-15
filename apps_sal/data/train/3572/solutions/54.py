def invite_more_women(arr):
    women=0
    men=0
    for i in arr:
        if i==-1:
            women=women+1
        else: 
            men=men+1
    if men>women:
        return True
    else:
        return False
