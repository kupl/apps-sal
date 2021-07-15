def my_first_kata(a,b):
    try:
        float(a)
        float(b)
        return a % b + b % a if a and b else False
    except:
        return False
