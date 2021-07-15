def my_first_kata(a,b):
    msg = False
    if isinstance(a,int) and isinstance(b,int) and a != 0 and b != 0:
        msg = a % b + b % a
    return msg
