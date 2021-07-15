from collections import Counter

def invite_more_women(arr):
    #your code here
    if arr == []:
        return False
    else:
        r = Counter(arr)
        if r[-1]>=r[1]:
           return False
        else:
           return True
           

