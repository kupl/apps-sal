def get_podpc():
    r=[]
    x=1
    while (x*x*x<=1e17):
        y=x*x*x
        if all(int(d)%2==1 for d in str(y)):
            r.append(y)
        x+=2
    return sorted([-1*x for x in r]+r)

arr=get_podpc()

def odd_dig_cubic(a, b):
    return [x for x in arr if a<=x<=b]
