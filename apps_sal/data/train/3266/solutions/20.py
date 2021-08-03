def my_first_kata(a, b):
    if str(a).isnumeric() is False or str(b).isnumeric() is False:
        return False
    else:
        return int(a) % int(b) + int(b) % int(a)
