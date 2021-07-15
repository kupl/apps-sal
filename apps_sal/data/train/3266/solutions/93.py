def my_first_kata(a,b):
    print(a, b)
    if str(a).isdigit() and str(b).isdigit():
        return int(a) % int(b) + int(b) % int(a)
    else:
        return False
