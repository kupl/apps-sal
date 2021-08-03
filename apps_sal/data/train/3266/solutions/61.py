def my_first_kata(a, b):
    if type(a) != int or type(b) != int:
        return False
    else:
        if a < b:
            return (a % b) + (b % a)
        else:
            return (b % a) + (a % b)
