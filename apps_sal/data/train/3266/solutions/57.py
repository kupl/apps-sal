def my_first_kata(a, b):
    try:
        if abs(float(a / 2 + b / 2)) > 0:
            return a % b + +b % a
        else:
            return False
    except:
        return False
