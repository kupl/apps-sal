def men_from_boys(arr):
    x=[x for x in arr if x%2==0]
    y=[x for x in arr if x%2!=0]
    a=list(set(x))
    b=list(set(y))
    b.sort(reverse=True)
    a.sort()
    
    return a+b
