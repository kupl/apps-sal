def my_first_kata(a, b):
    try:
        if complex(a) and complex(b):
            return a % b + b % a
        else:
            return False
    except:
        return False
