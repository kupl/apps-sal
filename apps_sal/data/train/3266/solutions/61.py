def my_first_kata(a, b):
    if type(a) != int or type(b) != int:
        return False
    elif a < b:
        return a % b + b % a
    else:
        return b % a + a % b
