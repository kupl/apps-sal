def my_first_kata(a,b):
    try:     
        return a % b + b % a
    except Exception:
        return False
