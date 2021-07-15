def array_leaders(numbers):
    right=0
    out=[]
    for x in numbers[::-1]:
        if x>right : out.append(x)
        right+=x
    return out[::-1]
