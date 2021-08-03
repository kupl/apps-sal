def my_first_kata(a, b):
    if str(a).isdigit() and str(b).isdigit():
        res = (a % b) + (b % a)
        return res
    else:
        return False
