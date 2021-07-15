def my_first_kata(a,b):
    if isinstance(a,int) and isinstance(b,int) and b != 0 and a != 0:
        return (a % b) + (b % a)
    else:
        return False
