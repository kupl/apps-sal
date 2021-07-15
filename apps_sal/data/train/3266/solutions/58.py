def my_first_kata(a,b):
    if isinstance(a, int) and isinstance(b, int)  :
        try: return a % b + b % a
        except :
            return False
    else : return False
