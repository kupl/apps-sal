def my_first_kata(a,b):
    if type(a) == type(b) == "number":
        return False
    try:
        return a % b + b % a
    except:
        return False
