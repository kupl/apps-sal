def is_smooth(n):
    for x in [2,3,5,7]:
        while n%x==0:n//=x
        if n==1:return ("power of 2",'3-smooth','Hamming number','humble number')[(2<x)+(3<x)+(5<x)]  
    return "non-smooth"
