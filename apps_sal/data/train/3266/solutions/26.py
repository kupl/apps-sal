def my_first_kata(a,b):
    try:
        if str(a).isdigit() and str(b).isdigit(): return (a % b) + (b % a)
        else:
            return False
    except:
        return False
