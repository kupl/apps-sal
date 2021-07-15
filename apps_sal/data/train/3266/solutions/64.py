def my_first_kata(a,b):
    if isinstance(a,int) and isinstance(b,int): 
        if a == 0 or b == 0: return False 
        if a is None or b is None: return False
        else: return (a%b + b%a)
    else: return False

