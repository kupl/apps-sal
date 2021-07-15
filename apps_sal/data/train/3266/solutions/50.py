def my_first_kata(a,b):
    try:
        x = a % b + b % a
        return x
    except:
        return False
