def men_from_boys(arr):
    arr=sorted(set(arr))
    a=[x for x in arr if x%2==0]
    b=sorted([x for x in arr if x%2==1],reverse=True)
    return a+b
