def men_from_boys(arr):
    arr=list(set(arr))
    return sorted([x for x in arr if abs(x)%2==0])+sorted([x for x in arr if abs(x)%2==1],reverse=True)
